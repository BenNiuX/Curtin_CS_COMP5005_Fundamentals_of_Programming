"""
testAnimals.py - test for animals.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - test for animals by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import time
import unittest

from matplotlib import pyplot as plt
from animals import Animal, Dog, Puppy, Squirrel
from config import Config
from container import Container


class TestAnimals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = Config()
        Container.init_obj(config)
        Container.init_stat()

    def test_animal(self):
        test_name = 'anim1'
        test_colour = 'grey'
        test_colour2 = 'white/grey'
        anim1 = Animal(test_name, test_colour)
        print(anim1)
        self.assertEqual(anim1.myclass, anim1.__class__.__name__)
        self.assertEqual(anim1.name, test_name)
        self.assertEqual(anim1.colour_pri, test_colour)
        self.assertEqual(anim1.colour_sec, test_colour)
        anim2 = Animal(test_name, test_colour2)
        print(anim2)
        self.assertEqual(anim2.colour_pri, test_colour2.split('/')[0])
        self.assertEqual(anim2.colour_sec, test_colour2.split('/')[1])

    def test_dog(self):
        test_name = 'dog1'
        test_colour = 'white'
        dog1 = Dog(test_name, test_colour)
        print(dog1)
        self.assertEqual(dog1.myclass, dog1.__class__.__name__)
        self.assertEqual(dog1.name, test_name)
        self.assertEqual(dog1.colour_pri, test_colour)
        self.assertEqual(dog1.colour_sec, test_colour)
        self.assertEqual(dog1.hungry, 0)
        self.assertEqual(dog1.thirsty, 0)
        self.assertEqual(dog1.lonely, 0)
        self.assertEqual(dog1.bored, 0)
        self.assertEqual(dog1.age, 0)
        self.assertEqual(dog1.counter, 0)
        self.assertTrue(dog1.is_thirsty())
        self.assertTrue(dog1.is_hungry())
        self.assertTrue(dog1.is_lonely())
        self.assertTrue(dog1.is_bored())
        self.assertTrue(dog1.is_thirsty())
        dog1.energy_degree(1)
        self.assertEqual(dog1.hungry, 0)
        self.assertEqual(dog1.thirsty, 0)
        self.assertEqual(dog1.lonely, 0)
        self.assertEqual(dog1.bored, 0)
        self.assertEqual(dog1.age, 0)
        dog1.hungry = 2
        dog1.thirsty = 2
        dog1.lonely = 2
        dog1.bored = 2
        dog1.energy_degree(1)
        self.assertEqual(dog1.hungry, 1)
        self.assertEqual(dog1.thirsty, 1)
        self.assertEqual(dog1.lonely, 1)
        self.assertEqual(dog1.bored, 1)

    def test_puppy(self):
        test_name = 'puppy1'
        test_colour = 'white'
        dog1 = Puppy(test_name, test_colour)
        print(dog1)
        self.assertEqual(dog1.myclass, dog1.__class__.__name__)
        self.assertEqual(dog1.name, test_name)
        self.assertEqual(dog1.colour_pri, test_colour)
        self.assertEqual(dog1.colour_sec, test_colour)

    def test_squirrel(self):
        test_name = 'squ1'
        test_colour = 'brown'
        squ1 = Squirrel(test_name)
        print(squ1)
        self.assertEqual(squ1.myclass, squ1.__class__.__name__)
        self.assertEqual(squ1.colour_pri, test_colour)
        self.assertEqual(squ1.colour_sec, test_colour)

    def test_plot(self):
        plt.ion()
        fig, ax = plt.subplots(figsize=(5, 5))
        for i in range(10):
            ax.set_title(f"Test plot: {i}")
            Container.plot_map(ax)
            Container.plot_obj(ax)

            fig.canvas.draw()
            fig.canvas.flush_events()
            ax.clear()
            time.sleep(1)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
