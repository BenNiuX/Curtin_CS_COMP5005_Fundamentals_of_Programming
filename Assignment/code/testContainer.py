"""
testContainer.py - test for container.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - initial version by Ben Niu 26/04/24
"""

import unittest
from common import Param
from config import Config
from container import Container


class TestContainer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = Config()
        Container.init_obj(config)
        Container.init_stat()

    def test_title(self):
        title = Container.get_title()
        print(title)
        self.assertTrue(title.startswith("Time"))
        self.assertTrue(title.endswith(" time"))

    def test_get_ymd_hms(self):
        Param.curr_time = 0
        (year, month, day), (hour, minu, sec) = Container.get_ymd_hms()
        self.assertEqual(year, 0)
        self.assertEqual(month, 0)
        self.assertEqual(day, 0)
        self.assertEqual(hour, 0)
        self.assertEqual(Container.get_hour(), 0)
        self.assertEqual(minu, 0)
        self.assertEqual(sec, 0)
        Param.curr_time = 61
        (year, month, day), (hour, minu, sec) = Container.get_ymd_hms()
        self.assertEqual(year, 0)
        self.assertEqual(month, 0)
        self.assertEqual(day, 0)
        self.assertEqual(hour, 0)
        self.assertEqual(Container.get_hour(), 0)
        self.assertEqual(minu, 1)
        self.assertEqual(sec, 1)
        Param.curr_time = (Param.YEAR + Param.MONTH + Param.DAY
                           + Param.HOUR + Param.MINUTE + 1)
        (year, month, day), (hour, minu, sec) = Container.get_ymd_hms()
        self.assertEqual(year, 1)
        self.assertEqual(month, 1)
        self.assertEqual(day, 1)
        self.assertEqual(hour, 1)
        self.assertEqual(Container.get_hour(), 1)
        self.assertEqual(minu, 1)
        self.assertEqual(sec, 1)

    def test_pause(self):
        self.assertFalse(Param.pause)
        self.assertFalse(Container.is_paused())
        Container.pause()
        self.assertTrue(Param.pause)
        self.assertTrue(Container.is_paused())


if __name__ == "__main__":
    unittest.main()
