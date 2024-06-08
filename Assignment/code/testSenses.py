"""
testSenses.py - test for senses.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - initial version by Ben Niu 26/04/24
"""

import time
import unittest

from matplotlib import pyplot as plt

from common import Param
from config import Config
from container import Container
from humans import Owner
from senses import Hear, Sight, Smell


class TestSenses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = Config()
        Container.init_obj(config)
        Container.init_stat()

    def test_smell(self):
        humans = Param.humans
        for human in humans:
            if isinstance(human, Owner):
                sense = Smell(10, Param.foods)
                plt.ion()
                fig, ax = plt.subplots(figsize=(5, 5))
                for i in range(10):
                    Param.curr_time += 1
                    if i == 0 or i == 3:
                        human.feed()
                    sense.get_next_step((1, 1))
                    ax.set_title(f"Test smell: {i}")
                    ax.imshow(sense.layer_array, cmap="hot")
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    ax.clear()
                    time.sleep(1)
        self.assertTrue(True)

    def test_hear(self):
        humans = Param.humans
        for human in humans:
            if isinstance(human, Owner):
                sense = Hear(10, Param.foods)
                plt.ion()
                fig, ax = plt.subplots(figsize=(5, 5))
                for i in range(10):
                    Param.curr_time += 1
                    if i == 0 or i == 3:
                        human.feed()
                    sense.get_next_step((1, 1))
                    ax.set_title(f"Test hear: {i}")
                    ax.imshow(sense.layer_array, cmap="hot")
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    ax.clear()
                    time.sleep(1)
        self.assertTrue(True)

    def test_sight(self):
        humans = Param.humans
        for human in humans:
            if isinstance(human, Owner):
                sense = Sight(10, Param.foods)
                plt.ion()
                fig, ax = plt.subplots(figsize=(5, 5))
                for i in range(10):
                    Param.curr_time += 1
                    if i == 0 or i == 3:
                        human.feed()
                    sense.get_next_step((1, 1))
                    ax.set_title(f"Test sight: {i}")
                    ax.imshow(sense.layer_array, cmap="hot")
                    fig.canvas.draw()
                    fig.canvas.flush_events()
                    ax.clear()
                    time.sleep(1)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
