"""
senses.py - define Sense class and subclasses

Written by : Ben Niu
Student ID : 21678145

Includes:
    Sense
    Sight
    Smell
    Hear

Versions:
    - implement Sight and Hear by Ben Niu 03/05/24
    - implement Smell by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import numpy as np
from common import Param, Position
from humans import Human


class Sense():
    """
    Define parent class of all senses.
    """
    myclass = "Sense"
    # Define value max as 100
    MAX_VALUE = 100

    def __init__(self, distance, objs):
        self.distance = distance
        self.last_update = 0
        self.objs = objs
        self.layer_array = np.zeros(Param.map.size)

    def get_next_step(self, posi_curr):
        # Need to be override to decide the next step/position.
        return None

    def update_sense_map(self):
        pass

    def fill_sense_array(self, pos, default_max=MAX_VALUE, step=-2):
        # Used to fill a 2D array with different numbers represent
        # sense degree.
        values = range(default_max, 0, step)
        (width, height) = self.layer_array.shape
        for i in range(len(values)):
            x1 = pos[0] - i
            x2 = pos[0] + i
            y1 = pos[1] - i
            y2 = pos[1] + i
            value = values[i]
            if x1 >= 0:
                for y in range(y1, y2+1):
                    if y >= 0 and y < height:
                        self.layer_array[x1, y] = max(
                            self.layer_array[x1, y], value)
            if x2 < width:
                for y in range(y1, y2+1):
                    if y >= 0 and y < height:
                        self.layer_array[x2, y] = max(
                            self.layer_array[x2, y], value)
            if y1 >= 0:
                for x in range(x1, x2+1):
                    if x >= 0 and x < width:
                        self.layer_array[x, y1] = max(
                            self.layer_array[x, y1], value)
            if y2 < height:
                for x in range(x1, x2+1):
                    if x >= 0 and x < width:
                        self.layer_array[x, y2] = max(
                            self.layer_array[x, y2], value)

    def __str__(self):
        return f"{self.myclass}"


class Sight(Sense):
    myclass = "Sight"

    def update_sense_map(self):
        if self.last_update != Param.curr_time:
            self.layer_array.fill(0)
            for obj in self.objs:
                self.fill_sense_array(obj.position)
            unavailable_area = ~Param.map.available_area
            self.layer_array[unavailable_area] = 0
            self.layer_array[Param.map.mask_house] = 0
            np.copyto(Param.debug_array, self.layer_array)

    def get_next_step(self, posi_curr):
        self.update_sense_map()
        mask_array = Position.gen_step_mask(
            self.layer_array, posi_curr, self.distance)
        (width, height) = self.layer_array.shape
        available_pos = []
        max_value = 0
        max_pos = None
        for i in range(width):
            for j in range(height):
                if mask_array[(i, j)]:
                    value = self.layer_array[(i, j)]
                    if max_value < value:
                        max_value = value
                        max_pos = (i, j)
                    available_pos.append((i, j))
        return max_pos


class Smell(Sense):
    myclass = "Smell"

    def update_sense_map(self):
        if self.last_update != Param.curr_time:
            self.layer_array.fill(0)
            for obj in self.objs:
                self.fill_sense_array(obj.position, int(
                    obj.INTEREST * (1 - 0.1 * obj.dig)))
            unavailable_area = ~Param.map.available_area
            self.layer_array[unavailable_area] = 0
            self.layer_array[Param.map.mask_house] = 0
            np.copyto(Param.debug_array, self.layer_array)

    def get_next_step(self, posi_curr):
        self.update_sense_map()
        mask_array = Position.gen_step_mask(
            self.layer_array, posi_curr, self.distance)
        (width, height) = self.layer_array.shape
        available_pos = []
        max_value = 0
        max_pos = None
        for i in range(width):
            for j in range(height):
                if mask_array[(i, j)]:
                    value = self.layer_array[(i, j)]
                    if max_value < value:
                        max_value = value
                        max_pos = (i, j)
                    available_pos.append((i, j))
        return max_pos


class Hear(Sense):
    myclass = "Hear"

    def update_sense_map(self):
        if self.last_update != Param.curr_time:
            self.layer_array.fill(0)
            for obj in self.objs:
                if isinstance(obj, Human):
                    if obj.DEFAULT_PLAY_PER_SEC > 0:
                        self.fill_sense_array(obj.position, step=-1)
                else:
                    self.fill_sense_array(obj.position, step=-1)
            unavailable_area = ~Param.map.available_area
            self.layer_array[unavailable_area] = 0
            # self.layer_array[Param.map.mask_house] = 0
            np.copyto(Param.debug_array, self.layer_array)

    def get_next_step(self, posi_curr):
        self.update_sense_map()
        mask_array = Position.gen_step_mask(
            self.layer_array, posi_curr, self.distance)
        (width, height) = self.layer_array.shape
        available_pos = []
        max_value = 0
        max_pos = None
        for i in range(width):
            for j in range(height):
                if mask_array[(i, j)]:
                    value = self.layer_array[(i, j)]
                    if max_value < value:
                        max_value = value
                        max_pos = (i, j)
                    available_pos.append((i, j))
        return max_pos
