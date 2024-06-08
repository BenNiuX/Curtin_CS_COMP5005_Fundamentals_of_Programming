"""
testCommon.py - test for common.py

Written by : Ben Niu
Student ID : 21678145

Usage:
    Execute py file

Versions:
    - initial version by Ben Niu 26/04/24
"""

import unittest

import numpy as np
from common import Param, Position
from config import Config
from container import Container


class TestCommon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config = Config()
        Container.init_obj(config)
        Container.init_stat()

    def test_position(self):
        test_posi = TestPosi()
        self.assertIsNone(test_posi.position)
        self.assertTrue(len(test_posi.posi_history) == 0)
        test_posi.next_step()
        self.assertEqual(test_posi.position, (1, 1))
        self.assertEqual(len(test_posi.posi_history), 1)
        test_posi.next_step()
        self.assertEqual(test_posi.position, (2, 2))
        self.assertEqual(len(test_posi.posi_history), 2)
        test_posi.next_step()
        self.assertEqual(test_posi.position, (3, 3))
        self.assertEqual(len(test_posi.posi_history), 3)
        test_posi.next_step()
        self.assertEqual(test_posi.position, (3, 3))
        self.assertEqual(len(test_posi.posi_history), 3)

    def test_position_close(self):
        test_posi = TestPosi()
        x, y = Param.doors[0].position
        test_posi.position = (x-1, y)
        self.assertTrue(test_posi.close_to_door())
        test_posi.position = (x-2, y)
        self.assertTrue(test_posi.close_to_door())
        test_posi.position = (x-2, y-1)
        self.assertFalse(test_posi.close_to_door())
        test_posi.position = (x, y-2)
        self.assertTrue(test_posi.close_to_door())
        x, y = Param.doors[1].position
        test_posi.position = (x-1, y)
        self.assertTrue(test_posi.close_to_door())
        test_posi.position = (x-2, y)
        self.assertTrue(test_posi.close_to_door())
        test_posi.position = (x-2, y-1)
        self.assertFalse(test_posi.close_to_door())
        test_posi.position = (x, y-2)
        self.assertTrue(test_posi.close_to_door())

    def test_distance(self):
        self.assertEqual(TestPosi.distance((1, 1), (1, 2), False), 1)
        self.assertEqual(TestPosi.distance((1, 1), (2, 2), False), 2)
        self.assertEqual(TestPosi.distance((1, 1), (1, 3), False), 2)
        self.assertEqual(TestPosi.distance((1, 1), (3, 1), False), 2)

    def test_near(self):
        self.assertEqual(TestPosi.get_near_pos((1, 1), (1, 2), (3, 3)), (1, 2))
        self.assertEqual(TestPosi.get_near_pos((1, 1), (2, 2), (3, 3)), (2, 2))
        self.assertEqual(TestPosi.get_near_pos((1, 1), (1, 3), (3, 3)), (1, 3))
        self.assertEqual(TestPosi.get_near_pos((1, 1), (3, 1), (3, 3)), (3, 1))

    def test_map(self):
        self.assertIsNotNone(Param.map.size)
        self.assertGreater(Param.map.width, 0)
        self.assertGreater(Param.map.height, 0)
        self.assertEqual(Param.map.array_data.shape, Param.map.size)

    def test_gen_step_mask(self):
        layer = np.zeros((5, 5))
        print(layer)
        check_result = [
            ((0, 0), [(0, 0), (0, 1), (1, 0), (1, 1)]),
            ((0, 1), [(0, 1), (0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]),
            ((0, 4), [(0, 3), (0, 4), (1, 3), (1, 4)]),
            ((1, 0), [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]),
            ((4, 0), [(3, 0), (3, 1), (4, 0), (4, 1)]),
            ((3, 1), [(2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0),
                      (4, 1), (4, 2)]),
            ((4, 4), [(4, 4), (3, 4), (4, 3), (3, 3)]),
        ]
        for item in check_result:
            mask = TestPosi.gen_step_mask(layer, item[0], 1)
            test = np.full((5, 5), fill_value=False)
            for i in item[1]:
                test[i] = True
            self.assertTrue(np.array_equal(mask, test), f"\n{mask}, \n{test}")
            print(TestPosi.gen_step_mask(layer, item[0], 2))


class TestPosi(Position):
    def __init__(self):
        super().__init__()
        self.steps = [(1, 1), (2, 2), (3, 3), (3, 3)]

    def decide_next_step(self):
        return self.steps.pop(0)


if __name__ == "__main__":
    unittest.main()
