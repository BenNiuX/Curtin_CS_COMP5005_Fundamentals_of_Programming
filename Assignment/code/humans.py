"""
humans.py - define Human class and subclasses

Written by : Ben Niu
Student ID : 21678145

Includes:
    Human
    Owner
    Friend
    Stranger
    Intruder

Versions:
    - implement Owner details by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import random
import matplotlib.patches as pat
from common import Map, Param, Position
from things import Bone, DogFood, Door, Food, Meat


class Human(Position):
    """
    Define parent class of all humans.

    This class extends from Position because Human and subclasses will be
    placed on the map and calculated distance with other position.
    """
    myclass = "Human"
    MAX_STEP = 5
    DEFAULT_PLAY_PER_SEC = 10

    def __init__(self, name, colour):
        super().__init__()
        self.name = name
        self.colour = colour
        self.priority = Param.PRIO_HUMAN

    def commu_per_sec(self, want):
        # Communicate with animails to increase their lonely value.
        ret = self.DEFAULT_PLAY_PER_SEC
        if want < ret:
            ret = want
        return ret

    def draw(self, ax, pos):
        patch = pat.Circle((pos[0], pos[1] - 1), radius=0.5, color="black")
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0], pos[1] + 0.2), height=2, width=1.5, color=self.colour
        )
        ax.add_patch(patch)

    def __str__(self):
        return self.name


class Owner(Human):
    """
    Define Owners class.
    """
    myclass = "Owner"
    COLOUR = "green"

    # Define activity parameter.
    ACTIVITY_FREE = 0
    ACTIVITY_OPEN_DOOR = 1
    ACTIVITY_CLOSE_DOOR = 2
    ACTIVITY_PLACE_FOOD = 3
    ACTIVITY_SLEEP = 4
    ACT_STR = ["Free", "Open", "Close", "Feed", "Sleep"]

    def __init__(self, name):
        super().__init__(name, self.COLOUR)
        self.next_activity = self.ACTIVITY_SLEEP
        self.position_next = []

    def maintain_door(self, state):
        # To open door or close door
        closed_doors = []
        ret = False
        for door in Param.doors:
            if door.state != state:
                closed_doors.append(door)
        if len(closed_doors) == 2:
            dist0 = self.distance(closed_doors[0].position, self.position)
            dist1 = self.distance(closed_doors[1].position, self.position)
            if dist0 <= dist1:
                self.target = closed_doors[0]
            else:
                self.target = closed_doors[1]
            if state == Door.STATE_OPEN:
                self.next_activity = self.ACTIVITY_OPEN_DOOR
            else:
                self.next_activity = self.ACTIVITY_CLOSE_DOOR
            ret = True
        elif len(closed_doors) == 1:
            self.target = closed_doors[0]
            if state == Door.STATE_OPEN:
                self.next_activity = self.ACTIVITY_OPEN_DOOR
            else:
                self.next_activity = self.ACTIVITY_CLOSE_DOOR
            ret = True
        return ret

    def place_food(self):
        # Prepare to place food in the yard.
        ret = False
        food_number = [3, 3]
        posis = []
        for i, num in enumerate(food_number):
            yard_mask = Param.map.mask_yard_back
            if i != 0:
                yard_mask = Param.map.mask_yard_front
            for i in range(num):
                posis.append(
                    self.gen_random_pos(Param.map.array_data,
                                        Map.GRASS, yard_mask)
                )
        if len(posis) > 0:
            self.target = posis
            self.next_activity = self.ACTIVITY_PLACE_FOOD
            ret = True
        return ret

    def feed(self):
        # Place food to feed animals.
        food_types = [Bone, Meat, DogFood]
        food_mass = random.choice(Food.AMOUNTS)
        food_dig = random.choice(Food.DIGES)
        food_type = random.choice(food_types)
        food = food_type()
        food.amount = food_mass
        food.dig = food_dig
        food.position = self.position
        Param.foods.append(food)

    def decide_next_step(self):
        """
        The most important method. This method will be called per second.
        This method is used to decide this human's next action/step.
        """
        if Param.time_sec == Param.TIME_SEC_EAT:
            if not self.target:
                ret = self.maintain_door(Door.STATE_OPEN)
                if not ret:
                    if len(Param.foods) == 0:
                        ret = self.place_food()
                if not ret:
                    self.next_activity = self.ACTIVITY_FREE
                    if self.target is None:
                        self.target = self.gen_random_pos(
                            Param.map.array_data,
                            Map.HOUSE,
                            Param.posi_record == Param.POSI_AVAILABLE,
                        )
        elif Param.time_sec == Param.TIME_SEC_PLAY:
            ret = self.maintain_door(Door.STATE_OPEN)
            if not ret:
                self.next_activity = self.ACTIVITY_FREE
                if self.target is None:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        Map.HOUSE,
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
        elif Param.time_sec == Param.TIME_SEC_SLEEP:
            if self.in_where(self.position) != Param.PLACE_HOUSE:
                self.target = self.gen_random_pos(
                    Param.map.array_data,
                    Map.HOUSE,
                    Param.posi_record == Param.POSI_AVAILABLE,
                )
                self.next_activity = self.ACTIVITY_FREE
            else:
                wait_dog = False
                dogs = []
                dogs.extend(Param.dogs)
                dogs.extend(Param.puppies)
                for dog in dogs:
                    if self.in_where(dog.position) != Param.PLACE_HOUSE:
                        wait_dog = True
                if wait_dog:
                    return None
                ret = self.maintain_door(Door.STATE_CLOSE)
                if not ret:
                    self.next_activity = self.ACTIVITY_FREE
                    if self.target is None and (
                        self.in_where(self.position) != Param.PLACE_HOUSE
                    ):
                        self.target = self.gen_random_pos(
                            Param.map.array_data,
                            Map.HOUSE,
                            Param.posi_record == Param.POSI_AVAILABLE,
                        )
                    else:
                        self.target = None
                        self.next_activity = self.ACTIVITY_SLEEP
            pass
        place_mask = self.get_place_mask(self.position)
        mask = Param.posi_record == Param.POSI_AVAILABLE
        if place_mask is not None and not self.close_to_door():
            mask = place_mask & mask
        next_posis = self.gen_next_positions(
            Param.map.array_data,
            [Map.HOUSE, Map.GRASS, Map.GARDEN],
            self.position,
            self.MAX_STEP,
            mask,
            # self.get_history_pos(),
        )
        if self.next_activity == self.ACTIVITY_FREE:
            next_posi = self.select_near_pos(next_posis, self.target)
            if self.distance(next_posi, self.target) < 2:
                self.target = None
                self.next_activity = self.ACTIVITY_FREE
                return None
            return next_posi
        elif self.next_activity == self.ACTIVITY_OPEN_DOOR:
            next_posi = self.select_near_pos(next_posis, self.target.position)
            if self.distance(next_posi, self.target.position) < 1:
                self.target.open()
                self.target = None
                self.next_activity = self.ACTIVITY_FREE
                return None
            return next_posi
        elif self.next_activity == self.ACTIVITY_CLOSE_DOOR:
            next_posi = self.select_near_pos(next_posis, self.target.position)
            if self.distance(next_posi, self.target.position) < 1:
                self.target.close()
                self.target = None
                self.next_activity = self.ACTIVITY_FREE
                return None
            return next_posi
        elif self.next_activity == self.ACTIVITY_PLACE_FOOD:
            min_d = 10000
            min_i = 0
            for i, item in enumerate(self.target):
                d = self.distance(self.position, item, False)
                if min_d > d:
                    min_i = i
                    min_d = d
            item = self.target.pop(min_i)
            self.target.insert(0, item)
            next_posi = self.select_near_pos(next_posis, self.target[0])
            if self.distance(next_posi, self.target[0]) == 0:
                self.feed()
                self.target.pop(0)
                if len(self.target) == 0:
                    self.target = None
                    self.next_activity = self.ACTIVITY_FREE
                    return None
            return next_posi

    def __str__(self):
        tmp = super().__str__()
        if self.next_activity is not None:
            return f"{tmp} {self.ACT_STR[self.next_activity]}"
        return tmp


class Friend(Human):
    myclass = "Friend"
    COLOUR = "blue"
    DEFAULT_PLAY_PER_SEC = 5

    def __init__(self, name):
        super().__init__(name, self.COLOUR)


class Stranger(Human):
    myclass = "Stranger"
    COLOUR = "orange"
    DEFAULT_PLAY_PER_SEC = 0

    def __init__(self, name):
        super().__init__(name, self.COLOUR)


class Intruder(Human):
    myclass = "Intruder"
    COLOUR = "red"
    DEFAULT_PLAY_PER_SEC = -1

    def __init__(self, name):
        super().__init__(name, self.COLOUR)
