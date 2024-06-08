"""
testThings.py - test for things.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - test for things by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import unittest

from config import Config
from container import Container
from things import Ball, Bone, DogFood, Door, Meat, Swing, Thing, Water


class TestThings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = Config()
        Container.init_obj(config)
        Container.init_stat()

    def test_thing(self):
        th = Thing("th")
        self.assertEqual(th.name, "th")

    def test_door(self):
        do_b = Door("do_b", Door.TYPE_BACK)
        do_f = Door("do_f", Door.TYPE_FRONT)
        self.assertEqual(do_f.name, "do_f")
        self.assertEqual(do_b.state, Door.STATE_CLOSE)
        do_b.open()
        self.assertEqual(do_b.state, Door.STATE_OPEN)
        do_b.close()
        self.assertEqual(do_b.state, Door.STATE_CLOSE)
        self.assertEqual(do_f.state, Door.STATE_CLOSE)
        do_f.close()
        self.assertEqual(do_f.state, Door.STATE_CLOSE)

    def test_water(self):
        wa = Water("wa")
        self.assertEqual(wa.name, "wa")
        self.assertEqual(wa.drink_per_sec(1), 1)
        self.assertEqual(wa.drink_per_sec(Water.DEFAULT_DRINK_PER_SEC + 1),
                         Water.DEFAULT_DRINK_PER_SEC)

    def test_food(self):
        bo = Bone()
        self.assertEqual(bo.INTEREST, Bone.INTEREST)
        me = Meat()
        self.assertEqual(me.INTEREST, Meat.INTEREST)
        df = DogFood()
        self.assertEqual(df.INTEREST, DogFood.INTEREST)
        df.dig = 2
        df.amount = 100
        self.assertFalse(df.is_eat_up())
        self.assertEqual(df.eat_per_sec(1), 0)
        self.assertEqual(df.amount, 100)
        self.assertEqual(df.eat_per_sec(1), 0)
        self.assertEqual(df.amount, 100)
        self.assertEqual(df.eat_per_sec(1), 1)
        self.assertEqual(df.amount, 99)
        self.assertEqual(df.eat_per_sec(df.DEFAULT_EAT_PER_SEC + 1),
                         df.DEFAULT_EAT_PER_SEC)
        self.assertEqual(df.amount, 99-df.DEFAULT_EAT_PER_SEC)
        me.amount = 5
        self.assertFalse(me.is_eat_up())
        self.assertEqual(me.eat_per_sec(10), 5)
        self.assertTrue(me.is_eat_up())

    def test_toy(self):
        sw = Swing("sw")
        self.assertEqual(sw.play_per_sec(1), 1)
        self.assertEqual(sw.play_per_sec(sw.DEFAULT_PLAY_PER_SEC + 1),
                         sw.DEFAULT_PLAY_PER_SEC)
        ba = Ball("ba", "red")
        self.assertEqual(ba.name, "ba")
        self.assertEqual(ba.colour, "red")
        self.assertEqual(ba.play_per_sec(1), 1)
        self.assertEqual(ba.play_per_sec(ba.DEFAULT_PLAY_PER_SEC + 1),
                         ba.DEFAULT_PLAY_PER_SEC)


if __name__ == "__main__":
    unittest.main()
