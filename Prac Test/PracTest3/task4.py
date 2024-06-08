"""
task4.py - program for task 4 in PracTest3

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

from creatures import Puppy, Cat

def build_yard(dims):
    plan = np.zeros(dims)
    plan[:, :] = 5
    plan[0, :] = 0
    plan[80, :] = 0
    plan[:, 0] = 0
    plan[:, -1] = 0
    plan[100:110, :] = 10
    plan[110:120, :] = 0
    plan[20:90, 20:70] = 7
    return plan

def build_yard2(dims):
    plan = np.zeros(dims)
    return plan
   
def update_smells(smells, creatures):
    for creature in creatures:
        pos = creature.get_pos()
        smells[pos[0], pos[1]] = 10

def plot_yard(ax, p):
    ax.imshow(p, cmap='nipy_spectral')

def plot_smells(ax, p):
    ax.imshow(p, cmap='hot')

def get_rand_pos(dims, creature):
    if creature == 'Cat':
        output = (random.randint(25, 35), random.randint(30, 60))
    else:
        output = (random.randint(5, 15), random.randint(10, dims[1]-10))
    print(f"input={dims}, output={output}")
    return output

def main():
    size = (120,90)
    yard = build_yard(size)
    smells = np.zeros(size)
    num_puppy = 7
    num_cat = 4
    num_simulation = 10
    creatures = []
    for i in range(num_puppy):
        creatures.append(Puppy("Snoopy_" + str(i+1), "white/black", get_rand_pos(size, 'Puppy')))
    for i in range(num_cat):
        creatures.append(Cat("Cat_" + str(i+1), "grey", get_rand_pos(size, 'Cat')))

    plt.ion()
    fig, (axs1, axs2) = plt.subplots(nrows=1, ncols=2, figsize=(15,10))
    for i in range(num_simulation):

        axs1.set_title(f"Task 3 Simulation: {i}")
        plot_yard(axs1, yard)

        for creature in creatures:
            creature.step_change()
            creature.plot_me(axs1, size)
        axs2.set_title(f"Smells: {i}")
        update_smells(smells, creatures)
        plot_smells(axs2, smells)

        fig.savefig("task4.png")

        fig.canvas.draw()           # this and following lines allow you
                                    # to refresh plot in the same window
        fig.canvas.flush_events()
        axs1.clear()
        axs2.clear()

        time.sleep(1)


if __name__ == "__main__":
    main()
