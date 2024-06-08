"""
creatures.py - class definitions for the creatures in FOP Assignment, Sem 1 2024

Written by : Ben Niu
Student ID : 21678145

Includes:
    Puppy
    Cat

Versions:
    - updated for PracTest3 by Ben Niu 16/04/24
    - initial version supplied 1/4/24
"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def flip_coords(pos, LIMITS):
    return((pos[1],pos[0]))
    #return pos

class Puppy():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-1,0),(1,1)]
        print(validmoves)
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self, ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        print(f"{self.pos} to {fpos}")
        ax.annotate(self.name, xy=(fpos[0]-1, fpos[1]-1.5), color="white", fontsize='x-small')
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]-0.9, fpos[1]-0.3), height=1.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Ellipse((fpos[0]+0.9, fpos[1]-0.3), height=1.5, width=0.3, color=self.colour2)
        ax.add_patch(patch)


class Cat():
    """
    Holds information and behaviour of cat creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def step_change(self):
        validmoves = [(-1,0), (1,0), (0,-1), (0,1)]
        print(validmoves)
        move = random.choice(validmoves)
        self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self, ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        print(f"{self.pos} to {fpos}")
        ax.annotate(self.name, xy=(fpos[0]-1, fpos[1]-1.5), color="white", fontsize='x-small')
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.6, fpos[1]-0.6), radius=0.5, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.6, fpos[1]-0.6), radius=0.5, color=self.colour2)
        ax.add_patch(patch)
