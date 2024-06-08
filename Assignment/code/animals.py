"""
animals.py - define Animal class and subclasses

Written by : Ben Niu
Student ID : 21678145

Includes:
    Animal
    Dog
    Puppy
    Squirrel
    Butterfly
    Ant

Versions:
    - implement Dog and Puppy's behaviors by Ben Niu 03/05/24
    - initial version by Ben Niu 26/04/24
"""

import matplotlib.patches as pat
from common import Map, Param, Position
from senses import Hear, Sight, Smell
from things import Door, Swing


class Animal(Position):
    """
    Define parent class of all animals.

    This class extends from Position because Animal and subclasses will be
    placed on the map and calculated distance with other position.
    """
    myclass = "Animal"

    # Define energy max as 100, and degree 1 after each 6 minutes.
    # STATE_VALUE_HIGH is used to check if hungry when current time isn't
    # feed time.
    STATE_VALUE_MAX = 100
    STATE_VALUE_HIGH = 80
    COUNTER_CYCLE = Param.MINUTE * 6

    def __init__(self, name, colour):
        super().__init__()
        self.name = name
        self.parse_colour(colour)
        # Define feel status, cover hungry, thirsty, lonely and bored.
        self.hungry = 0
        self.thirsty = 0
        self.lonely = 0
        self.bored = 0
        # Define count status like age. counter is used to record
        # energy degree.
        self.age = 0
        self.counter = 0
        # Define senses, cover smell, sight and hear.
        self.smell = None
        self.sight = None
        self.hear = None

    def is_hungry(self):
        if Param.time_sec == Param.TIME_SEC_EAT:
            return self.hungry < self.STATE_VALUE_MAX
        return self.hungry < self.STATE_VALUE_HIGH

    def is_thirsty(self):
        if Param.time_sec == Param.TIME_SEC_EAT:
            return self.thirsty < self.STATE_VALUE_MAX
        return self.thirsty < self.STATE_VALUE_HIGH

    def is_bored(self):
        if Param.time_sec == Param.TIME_SEC_PLAY:
            return self.bored < self.STATE_VALUE_MAX
        return self.bored < self.STATE_VALUE_HIGH

    def is_lonely(self):
        if Param.time_sec == Param.TIME_SEC_PLAY:
            return self.lonely < self.STATE_VALUE_MAX
        return self.lonely < self.STATE_VALUE_HIGH

    def parse_colour(self, colour):
        colsplit = colour.split("/")
        self.colour_pri = colsplit[0]
        self.colour_sec = colsplit[0]
        if len(colsplit) > 1:
            self.colour_sec = colsplit[1]

    def energy_degree(self, degree):
        """
        Reduce energy status.
        """
        if self.hungry >= degree:
            self.hungry -= degree
        else:
            self.hungry = 0
        if self.thirsty >= degree:
            self.thirsty -= degree
        else:
            self.thirsty = 0
        if self.lonely >= degree:
            self.lonely -= degree
        else:
            self.lonely = 0
        if self.bored >= degree:
            self.bored -= degree
        else:
            self.bored = 0

    def check_energy(self):
        """
        Check if it's time to degree energy.
        """
        degree = self.counter // self.COUNTER_CYCLE
        if degree > 0:
            self.energy_degree(degree)
            self.counter = self.counter % self.COUNTER_CYCLE

    def time_changed(self, old_time, new_time, sec):
        """
        When time set to the future, this function will be called
        to update status.
        """
        self.age += sec
        self.counter += sec
        self.check_energy()

    def decide_next_step(self):
        """
        Overlay this method to count 1 second passed and check
        if energy should degree.
        """
        self.age += 1
        self.counter += 1
        self.check_energy()

    def __str__(self):
        return self.name


class Dog(Animal):
    """
    Define Dog class.
    """
    myclass = "Dog"
    # The max step moved per second.
    MAX_STEP = 3
    # Define each sense distance, like dog could smell max to 10 steps.
    SMELL_DISTANCE = 10
    SIGHT_DISTANCE = 20
    HEAR_DISTANCE = 30

    # Define activity parameter.
    ACTIVITY_FREE = 0
    ACTIVITY_SMELL = 1
    ACTIVITY_DRINK = 2
    ACTIVITY_PLAY = 3
    ACTIVITY_TAKE = 4
    ACTIVITY_COMP = 5
    ACTIVITY_SLEEP = 6
    ACTIVITY_FORCE = 10
    ACT_STR = [
        "Free",
        "Smell",
        "Drink",
        "Play",
        "Take",
        "Comp",
        "Sleep",
        "",
        "",
        "",
        "Force",
    ]

    # When animal reach the target within the distance of threshold.
    DISTANCE_THRESHOLD = 2

    def __init__(self, name, colour):
        super().__init__(name, colour)
        # Priority is used to detect collision.
        self.priority = Param.PRIO_DOG
        self.target = None
        self.next_activity = self.ACTIVITY_SLEEP
        # Record the toy taken by animal.
        self.take = None
        # Sense instances. Foods are found by smell, toys are found by sight,
        # water and humans are found by hear.
        self.smell = Smell(self.SMELL_DISTANCE, Param.foods)
        self.sight = Sight(self.SIGHT_DISTANCE, Param.toys)
        self.hear_water = Hear(self.HEAR_DISTANCE, Param.waters)
        self.hear_commu = Hear(self.HEAR_DISTANCE, Param.humans)

    def draw(self, ax, pos):
        patch = pat.Circle(pos, radius=1.5, color=self.colour_pri)
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0] - 0.9, pos[1] - 0.6), height=2, width=0.3,
            color=self.colour_sec
        )
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0] + 0.9, pos[1] - 0.6), height=2, width=0.3,
            color=self.colour_sec
        )
        ax.add_patch(patch)

    def eat(self, food):
        delta = food.eat_per_sec(self.STATE_VALUE_MAX - self.hungry)
        self.hungry += delta
        if self.hungry > self.STATE_VALUE_MAX:
            self.hungry = self.STATE_VALUE_MAX

    def drink(self, water):
        delta = water.drink_per_sec(self.STATE_VALUE_MAX - self.thirsty)
        self.thirsty += delta
        if self.thirsty > self.STATE_VALUE_MAX:
            self.thirsty = self.STATE_VALUE_MAX

    def play(self, toy):
        delta = toy.play_per_sec(self.STATE_VALUE_MAX - self.bored)
        self.bored += delta
        if self.bored > self.STATE_VALUE_MAX:
            self.bored = self.STATE_VALUE_MAX

    def commu(self, human):
        delta = human.commu_per_sec(self.STATE_VALUE_MAX - self.lonely)
        self.lonely += delta
        if self.lonely > self.STATE_VALUE_MAX:
            self.lonely = self.STATE_VALUE_MAX

    def take_toy(self, toy):
        self.take = toy

    def release_toy(self):
        # Release toy if animal take one.
        if self.take:
            self.take.taken(None)
            self.take_toy(None)

    def decide_next_step(self):
        super().decide_next_step()
        step = self.decide_next_step_inner()
        return step

    def decide_next_step_inner(self):
        """
        The most important method. This method will be called per second.
        This method is used to decide this animal's next action/step.
        """
        if self.in_where(self.position) == Param.PLACE_HOUSE:
            wait_door = False
            for door in Param.doors:
                if door.state == Door.STATE_CLOSE:
                    wait_door = True
            if wait_door:
                return None
        if self.next_activity == self.ACTIVITY_FORCE:
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
            )
            next_posi = self.select_near_pos(next_posis, self.target)
            if self.distance(next_posi, self.target) < self.DISTANCE_THRESHOLD:
                self.next_activity = self.ACTIVITY_FREE
                if Param.time_sec == Param.TIME_SEC_SLEEP:
                    self.next_activity = self.ACTIVITY_SLEEP
                self.target = None
                return None
            if Param.time_sec != Param.TIME_SEC_SLEEP \
                    and self.in_similar_place(self.target, self.position):
                self.next_activity = self.ACTIVITY_FREE
                self.target = None
                return None
            return next_posi
        elif Param.time_sec == Param.TIME_SEC_EAT:
            if self.is_hungry():
                if self.target is None:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        Map.GRASS,
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
                self.next_activity = self.ACTIVITY_SMELL
            elif self.is_thirsty():
                if self.target is None:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        Map.GRASS,
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
                self.next_activity = self.ACTIVITY_DRINK
            else:
                if self.target is None:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        [Map.GRASS, Map.HOUSE],
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
                self.next_activity = self.ACTIVITY_FREE

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
            if self.next_activity == self.ACTIVITY_SMELL:
                smell_next_posi = self.smell.get_next_step(self.position)
                if smell_next_posi:
                    if not self.in_similar_place(smell_next_posi,
                                                 self.position):
                        self.target = smell_next_posi
                        self.next_activity = self.ACTIVITY_FORCE
                    self.target = smell_next_posi
                    next_posi = self.select_near_pos(next_posis, self.target)
                    foods = Param.foods
                    for food in foods:
                        if (
                            self.distance(next_posi, food.position)
                            < self.DISTANCE_THRESHOLD
                        ):
                            self.eat(food)
                            self.target = None
                            return None
                    return next_posi
                else:
                    next_posi = self.select_near_pos(next_posis, self.target)
                    if (
                        self.distance(next_posi, self.target)
                        < self.DISTANCE_THRESHOLD
                    ):
                        self.target = None
                        return None
                    return next_posi
            elif self.next_activity == self.ACTIVITY_DRINK:
                hear_next_posi = self.hear_water.get_next_step(self.position)
                if hear_next_posi:
                    if not self.in_similar_place(hear_next_posi,
                                                 self.position):
                        self.target = hear_next_posi
                        self.next_activity = self.ACTIVITY_FORCE
                    self.target = hear_next_posi
                    next_posi = self.select_near_pos(next_posis, self.target)
                    waters = Param.waters
                    for water in waters:
                        if (
                            self.distance(next_posi, water.position)
                            < self.DISTANCE_THRESHOLD
                        ):
                            self.drink(water)
                            self.target = None
                            return None
                    return next_posi
                else:
                    next_posi = self.select_near_pos(next_posis, self.target)
                    if (
                        self.distance(next_posi, self.target)
                        < self.DISTANCE_THRESHOLD
                    ):
                        self.target = None
                        return None
                    return next_posi
            else:
                next_posi = self.select_near_pos(next_posis, self.target)
                if (
                    self.distance(next_posi, self.target)
                    < self.DISTANCE_THRESHOLD
                ):
                    self.target = None
                    return None
                else:
                    return next_posi

        elif Param.time_sec == Param.TIME_SEC_PLAY:
            if self.next_activity == self.ACTIVITY_TAKE:
                pass
            elif self.is_bored():
                if self.target is None:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        Map.GRASS,
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
                self.next_activity = self.ACTIVITY_PLAY
            elif self.is_lonely():
                if self.target is None:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        Map.GRASS,
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
                self.next_activity = self.ACTIVITY_COMP
            else:
                if not self.target:
                    self.target = self.gen_random_pos(
                        Param.map.array_data,
                        [Map.GRASS, Map.HOUSE],
                        Param.posi_record == Param.POSI_AVAILABLE,
                    )
                self.next_activity = self.ACTIVITY_FREE

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

            if self.next_activity == self.ACTIVITY_PLAY:
                sight_next_posi = self.sight.get_next_step(self.position)
                if sight_next_posi:
                    if not self.in_similar_place(sight_next_posi,
                                                 self.position):
                        self.target = sight_next_posi
                        self.next_activity = self.ACTIVITY_FORCE
                    self.target = sight_next_posi
                    next_posi = self.select_near_pos(next_posis, self.target)
                    toys = Param.toys
                    for toy in toys:
                        if (
                            self.distance(next_posi, toy.position)
                            < self.DISTANCE_THRESHOLD
                        ):
                            self.play(toy)
                            if not isinstance(toy, Swing):
                                self.next_activity = self.ACTIVITY_TAKE
                                self.take_toy(toy)
                                toy.taken(self)
                                self.target = self.gen_random_pos(
                                    Param.map.array_data,
                                    Map.GRASS,
                                    Param.posi_record == Param.POSI_AVAILABLE
                                )
                                while not self.in_similar_place(
                                    self.target, self.position
                                ):
                                    tmp_mask = Param.posi_record \
                                         == Param.POSI_AVAILABLE
                                    self.target = self.gen_random_pos(
                                        Param.map.array_data,
                                        Map.GRASS,
                                        tmp_mask
                                    )
                                return None
                            else:
                                self.target = None
                                return None
                    return next_posi
                else:
                    next_posi = self.select_near_pos(next_posis, self.target)
                    if (
                        self.distance(next_posi, self.target)
                        < self.DISTANCE_THRESHOLD
                    ):
                        self.target = None
                        return None
                    return next_posi
            elif self.next_activity == self.ACTIVITY_TAKE:
                next_posi = self.select_near_pos(next_posis, self.target)
                self.play(self.take)
                if (
                    self.distance(next_posi, self.target)
                    < self.DISTANCE_THRESHOLD or not self.is_bored()
                ):
                    self.release_toy()
                    self.next_activity = self.ACTIVITY_FREE
                    self.target = None
                    return None
                return next_posi
            elif self.next_activity == self.ACTIVITY_COMP:
                hear_next_posi = self.hear_commu.get_next_step(self.position)
                if hear_next_posi:
                    if not self.in_similar_place(hear_next_posi,
                                                 self.position):
                        self.target = hear_next_posi
                        self.next_activity = self.ACTIVITY_FORCE
                    self.target = hear_next_posi
                    next_posi = self.select_near_pos(next_posis, self.target)
                    humans = Param.humans
                    for human in humans:
                        if (
                            self.distance(next_posi, human.position)
                            < self.DISTANCE_THRESHOLD
                        ):
                            self.commu(human)
                            self.target = None
                            return None
                    return next_posi
                else:
                    next_posi = self.select_near_pos(next_posis, self.target)
                    if (
                        self.distance(next_posi, self.target)
                        < self.DISTANCE_THRESHOLD
                    ):
                        self.target = None
                        return None
                    return next_posi
            else:
                next_posi = self.select_near_pos(next_posis, self.target)
                if (
                    self.distance(next_posi, self.target)
                    < self.DISTANCE_THRESHOLD
                ):
                    self.target = None
                    return None
                else:
                    return next_posi
        elif Param.time_sec == Param.TIME_SEC_SLEEP:
            self.release_toy()
            if self.in_where(self.position) == Param.PLACE_HOUSE:
                self.next_activity = self.ACTIVITY_SLEEP
                self.target = None
            else:
                self.next_activity = self.ACTIVITY_FORCE
                self.target = self.gen_random_pos(
                    Param.map.array_data,
                    Map.HOUSE,
                    Param.posi_record == Param.POSI_AVAILABLE,
                )

    def __str__(self):
        tmp = super().__str__()
        tmp = f"{tmp} H:{self.hungry} T:{self.thirsty}" \
            f" B:{self.bored} L:{self.lonely}"
        if self.next_activity is not None:
            return f"{tmp} {self.ACT_STR[self.next_activity]}"
        return tmp


class Puppy(Dog):
    myclass = "Puppy"
    # The max step moved per second, override parent definition
    MAX_STEP = 1
    # Override distances
    SMELL_DISTANCE = 5
    SIGHT_DISTANCE = 10
    HEAR_DISTANCE = 15

    def __init__(self, name, colour):
        super().__init__(name, colour)
        self.priority = Param.PRIO_PUPPY

    def draw(self, ax, pos):
        patch = pat.Circle(pos, radius=1, color=self.colour_pri)
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0] - 0.9, pos[1] - 0.3), height=1.5, width=0.3,
            color=self.colour_sec
        )
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0] + 0.9, pos[1] - 0.3), height=1.5, width=0.3,
            color=self.colour_sec
        )
        ax.add_patch(patch)


class Squirrel(Animal):
    myclass = "Squirrel"
    COLOR = "brown"

    def __init__(self, name):
        super().__init__(name, self.COLOR)
        self.priority = Param.PRIO_SQUIRREL

    def draw(self, ax, pos):
        patch = pat.Circle(pos, radius=1, color=self.colour_pri)
        ax.add_patch(patch)
        patch = pat.Circle(
            (pos[0] - 0.6, pos[1] - 0.6), radius=0.8, color=self.colour_sec
        )
        ax.add_patch(patch)
        patch = pat.Circle(
            (pos[0] + 0.6, pos[1] - 0.6), radius=0.8, color=self.colour_sec
        )
        ax.add_patch(patch)


class ButterFly(Animal):
    myclass = "ButterFly"


class Ant(Animal):
    myclass = "Ant"
