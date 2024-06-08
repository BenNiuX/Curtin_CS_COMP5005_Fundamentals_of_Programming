"""
task1.py - program for task 1 in PracTest3

Written by : Ben Niu
Student ID : 21678145

Usage:

Versions:
    - updated for PracTest3 by Ben Niu 16/04/24
    - initial version supplied 15/4/24
"""
import numpy as np
import matplotlib.pyplot as plt
import time
import random

from creatures import Puppy

def build_yard(dims):
    plan = np.zeros(dims)
    return plan

def build_yard2(dims):
    plan = np.zeros(dims)
    return plan
   
def update_smells(smells, creatures):
    pass

def plot_yard(ax, p):
    ax.imshow(p)

def plot_smells(ax, p):
    ax.imshow(p)

def get_rand_pos(dims):
    output = (random.randint(10, 20), random.randint(10, dims[1]-10))
    print(f"input={dims}, output={output}")
    return output

def main():
    size = (60,70)
    yard = build_yard(size)
    smells = np.zeros(size)
    num_puppy = 7
    num_simulation = 10
    creatures = []
    for i in range(num_puppy):
        creatures.append(Puppy("Snoopy_" + str(i+1), "white/black", get_rand_pos(size)))

    plt.ion()
    fig, axs = plt.subplots(figsize=(15,10))
    for i in range(num_simulation):

        axs.set_title(f"Task 1 Simulation: {i}")

        plot_yard(axs, yard)

        for creature in creatures:
            creature.plot_me(axs, size)
            creature.step_change()
        
        fig.savefig("task1.png")

        fig.canvas.draw()           # this and following lines allow you
                                    # to refresh plot in the same window
        fig.canvas.flush_events()
        axs.clear()

        time.sleep(1)


if __name__ == "__main__":
    main()
