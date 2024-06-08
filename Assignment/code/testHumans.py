"""
testHumans.py - test for humans.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - test for humans by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import unittest

from common import Param
from config import Config
from container import Container
from humans import Human, Owner


class TestHumans(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = Config()
        Container.init_obj(config)
        Container.init_stat()

    def test_human(self):
        human = Human("h1", "red")
        self.assertEqual(human.name, "h1")
        self.assertEqual(human.colour, "red")
        self.assertEqual(human.commu_per_sec(1), 1)
        self.assertEqual(human.commu_per_sec(human.DEFAULT_PLAY_PER_SEC + 1),
                         human.DEFAULT_PLAY_PER_SEC)

    def test_feed(self):
        humans = Param.humans
        for human in humans:
            if isinstance(human, Owner):
                self.assertEqual(len(Param.foods), 0)
                human.feed()
                self.assertEqual(len(Param.foods), 1)
                human.feed()
                self.assertEqual(len(Param.foods), 2)


if __name__ == "__main__":
    unittest.main()
