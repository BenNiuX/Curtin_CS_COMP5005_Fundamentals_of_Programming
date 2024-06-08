"""
things.py - define Thing class and subclasses

Written by : Ben Niu
Student ID : 21678145

Includes:
    Thing
    Door
    Water
    Food
    Bone
    Meat
    DogFood
    Toy
    Swing
    Ball

Versions:
    - implement Toy and subclasses by Ben Niu 02/05/24
    - implement Door, Food and subclasses by Ben Niu 01/05/24
    - initial version by Ben Niu 26/04/24
"""

import matplotlib.patches as pat
from common import Position


class Thing(Position):
    """
    Define parent class of all Thing.

    This class extends from Position because Thing and subclasses will be
    placed on the map and calculated distance with other position.
    """
    myclass = "Thing"

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name


class Door(Thing):
    myclass = "Door"
    STATE_CLOSE = 0
    STATE_OPEN = 1
    TYPE_FRONT = 0
    TYPE_BACK = 1

    def __init__(self, name, type):
        super().__init__(name)
        self.state = self.STATE_CLOSE
        self.type = type

    def open(self):
        self.state = self.STATE_OPEN

    def close(self):
        self.state = self.STATE_CLOSE

    def draw(self, ax, pos):
        if self.state == self.STATE_CLOSE:
            patch = pat.Rectangle(
                (pos[0], pos[1] - 1), width=3, height=1, color="black"
            )
            ax.add_patch(patch)
            patch = pat.Rectangle(
                (pos[0] - 3, pos[1] - 1), width=3, height=1, color="black"
            )
            ax.add_patch(patch)
        elif self.state == self.STATE_OPEN:
            patch = pat.Rectangle(
                (pos[0] + 3, pos[1] - 1), width=3, height=1, color="black"
            )
            ax.add_patch(patch)
            patch = pat.Rectangle(
                (pos[0] - 6, pos[1] - 1), width=3, height=1, color="black"
            )
            ax.add_patch(patch)

    def __str__(self):
        state = "Open" if self.state == self.STATE_OPEN else "Close"
        return f"{self.name}:{state}"


class Water(Thing):
    myclass = "Water"
    DEFAULT_DRINK_PER_SEC = 10

    def draw(self, ax, pos):
        patch = pat.Rectangle((pos[0], pos[1]), width=1,
                              height=1.3, color="lightblue")
        ax.add_patch(patch)

    def drink_per_sec(self, want):
        ret = self.DEFAULT_DRINK_PER_SEC
        if want < ret:
            ret = want
        return ret


class Food(Thing):
    myclass = "Food"
    AMOUNTS = [80, 60, 40]
    DIGES = [0, 1, 2]
    DEFAULT_EAT_PER_SEC = 10
    INTEREST = 100

    def __init__(self):
        super().__init__(self.myclass)
        self.amount = 0
        self.dig = 0

    def eat_per_sec(self, want):
        if self.dig > 0:
            self.dig -= 1
            return 0

        ret = self.DEFAULT_EAT_PER_SEC
        if self.amount < self.DEFAULT_EAT_PER_SEC:
            ret = self.amount
        if ret > want:
            ret = want
        self.amount -= ret
        return ret

    def is_eat_up(self):
        return self.amount <= 0

    def __str__(self):
        tmp = super().__str__()
        tmp = f"{tmp} {self.amount} {self.dig}"
        return tmp


class Bone(Food):
    myclass = "Bone"
    INTEREST = 80

    def draw(self, ax, pos):
        patch = pat.Rectangle(
            (pos[0] - 0.5, pos[1] - 0.2), width=1, height=0.4, color="white"
        )
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0] - 0.5, pos[1]), height=0.7, width=0.3, color="white"
        )
        ax.add_patch(patch)
        patch = pat.Ellipse(
            (pos[0] + 0.5, pos[1]), height=0.7, width=0.3, color="white"
        )
        ax.add_patch(patch)


class Meat(Food):
    myclass = "Meat"

    def draw(self, ax, pos):
        patch = pat.Ellipse(pos, height=1, width=1.5, color="pink")
        ax.add_patch(patch)


class DogFood(Food):
    myclass = "DogFood"
    INTEREST = 60

    def draw(self, ax, pos):
        patch = pat.Circle((pos[0] - 0.25, pos[1] - 0.25),
                           radius=0.15, color="brown")
        ax.add_patch(patch)
        patch = pat.Circle((pos[0] + 0.25, pos[1] - 0.25),
                           radius=0.15, color="brown")
        ax.add_patch(patch)
        patch = pat.Circle((pos[0] - 0.25, pos[1] + 0.25),
                           radius=0.15, color="brown")
        ax.add_patch(patch)
        patch = pat.Circle((pos[0] + 0.25, pos[1] + 0.25),
                           radius=0.15, color="brown")
        ax.add_patch(patch)


class Toy(Thing):
    myclass = "Toy"
    DEFAULT_PLAY_PER_SEC = 10

    def play_per_sec(self, want):
        ret = self.DEFAULT_PLAY_PER_SEC
        if want < ret:
            ret = want
        return ret


class Swing(Toy):
    myclass = "Swing"

    def draw(self, ax, pos):
        patch = pat.Rectangle(
            (pos[0] - 1, pos[1] - 0.4), width=2, height=0.05, color="black"
        )
        ax.add_patch(patch)
        patch = pat.Rectangle(
            (pos[0] - 0.3, pos[1] - 0.4), width=0.05, height=1.5, color="black"
        )
        ax.add_patch(patch)
        patch = pat.Rectangle(
            (pos[0] + 0.3, pos[1] - 0.4), width=0.05, height=1.5, color="black"
        )
        ax.add_patch(patch)
        patch = pat.Rectangle(
            (pos[0] - 0.4, pos[1] + 1), width=0.8, height=0.1, color="black"
        )
        ax.add_patch(patch)


class Ball(Toy):
    myclass = "Ball"
    DEFAULT_PLAY_PER_SEC = 5

    def __init__(self, name, colour):
        super().__init__(name)
        self.colour = colour
        self.taken_anim = None

    def taken(self, anim):
        self.taken_anim = anim

    def decide_next_step(self):
        if self.taken_anim:
            return self.taken_anim.position
        else:
            self.posi_history = []

    def draw(self, ax, pos):
        patch = pat.Circle(pos, radius=0.7, color=self.colour)
        ax.add_patch(patch)
        patch = pat.Circle(pos, radius=0.3, color="brown")
        ax.add_patch(patch)
