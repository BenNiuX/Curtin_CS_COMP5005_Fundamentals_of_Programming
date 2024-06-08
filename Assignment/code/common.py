"""
common.py - define common classes

Written by:Ben Niu
Student ID:21678145

Includes:
    Param
    Map
    Position

Versions:
    - implement Map and Position by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import random
import numpy as np

from exceptions import PositionException


class Param():

    # Define time counter related params.
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    MONTH = DAY * 30
    YEAR = MONTH * 12

    # Define position record values.
    POSI_AVAILABLE = 0
    POSI_UNAVAILABLE = 1

    # Define difference time sections over 1 day.
    TIME_SEC_UNKNOWN = 0
    TIME_SEC_SLEEP = 1
    TIME_SEC_EAT = 2
    TIME_SEC_PLAY = 3
    TIME_SECS = ["Unknown", "Sleep time", "Feed time", "Play time"]

    # Define difference priorities for different creatures.
    PRIO_HUMAN = 10
    PRIO_DOG = 8
    PRIO_PUPPY = 6
    PRIO_SQUIRREL = 4
    PRIO_LOWEST = 0

    # Define recording history position.
    POSI_HISTORY = 5
    POSI_HISTORY_MAX = 10

    # Define ID used for place.
    PLACE_UNKNOWN = 0
    PLACE_HOUSE = 1
    PLACE_YARD_BACK = 2
    PLACE_YARD_FRONT = 3
    PLACE_TO_STR = ["UNKNOWN", "HOUSE", "YARD_BACK", "YARD_FRONT"]


class Position():
    """
    Define Position class to handling position or coordinate.
    """
    @classmethod
    def flip_coords(cls, pos):
        return (pos[1], pos[0])

    def __init__(self):
        self.position = None
        self.priority = Param.PRIO_LOWEST
        self.target = None
        self.posi_history = []

    def draw(self, ax, pos):
        # Need to be override to draw the creature.
        pass

    def decide_next_step(self):
        # Need to be override to decide next step position.
        # Need return a new position.
        pass

    def next_step(self):
        # Will be called per second.
        new_pos = self.decide_next_step()
        if not new_pos or new_pos == self.position:
            pass
        else:
            Param.posi_record[self.position] = Param.POSI_AVAILABLE
            Param.posi_record[new_pos] = Param.POSI_UNAVAILABLE
            self.posi_history.append(self.position)
            if len(self.posi_history) > Param.POSI_HISTORY_MAX:
                self.posi_history.pop(0)
            self.position = new_pos

    def time_changed(self, old_time, new_time, sec):
        # This function will be called when time changed.
        # Need to override if creature interest time changed event.
        pass

    def get_history_pos(self, num=Param.POSI_HISTORY):
        return self.posi_history[-num:]

    def plot(self, ax):
        # Used to draw creature on the figure.
        if not self.position:
            return
        pos = self.flip_coords(self.position)
        ax.annotate(
            self, xy=(pos[0] - 1, pos[1] - 1.5), color="black",
            fontsize="x-small"
        )
        self.draw(ax, pos)

    def close_to_door(self):
        # Used to draw creature on the figure.
        return (
            self.distance(self.position, Param.doors[0].position) <= 2
            or self.distance(self.position, Param.doors[1].position) <= 2
        )

    @classmethod
    def gen_mask(cls, map_array, avail_types, avail_pos=None):
        """
        Generate mask by given which type could be available,
        like GRASS, HOUSE.
        Param avail_pos allow specify more mask.
        """
        (width, height) = map_array.shape
        mask_array = np.full(shape=(width, height), fill_value=False)
        if isinstance(avail_types, int):
            avail_types = [avail_types]
        if len(avail_types) == 0:
            mask_array[:, :] = True
        else:
            for avail_type in avail_types:
                mask_array = (map_array == avail_type) | mask_array
        if avail_pos is not None:
            (avail_width, avail_height) = avail_pos.shape
            if not (avail_width == width and avail_height == height):
                print(f"not match: {map_array.shape} vs. {avail_pos}")
            else:
                mask_array = mask_array & avail_pos
        return mask_array

    @classmethod
    def gen_step_mask(cls, map_array, pos, max_step):
        """
        Generate mask by step. This mask could be used to calcuate next step.
        """
        (width, height) = map_array.shape
        mask_array = np.full(shape=(width, height), fill_value=False)
        x_start = pos[0] - max_step
        if x_start < 0:
            x_start = 0
        x_end = pos[0] + max_step
        if x_end >= width:
            x_end = width - 1
        y_start = pos[1] - max_step
        if y_start < 0:
            y_start = 0
        y_end = pos[1] + max_step
        if y_end >= height:
            y_end = height - 1
        mask_array[x_start:x_end+1, y_start:y_end+1] = True
        return mask_array

    @classmethod
    def in_where(cls, pos):
        """
        Check this position belongs to which place, like house, back yard.
        """
        ret = Param.PLACE_UNKNOWN
        if pos is None:
            raise PositionException("Pos is None")
        else:
            try:
                if Param.map.mask_house[pos]:
                    ret = Param.PLACE_HOUSE
                if Param.map.mask_yard_back[pos]:
                    ret = Param.PLACE_YARD_BACK
                if Param.map.mask_yard_front[pos]:
                    ret = Param.PLACE_YARD_FRONT
            except ValueError as e:
                print(e)
        if ret == Param.PLACE_UNKNOWN:
            print("in_where:", pos, Param.PLACE_TO_STR[ret])
        return ret

    @classmethod
    def get_place_mask(cls, pos):
        """
        Get place mask by position.
        """
        where = cls.in_where(pos)
        ret = None
        if where == Param.PLACE_HOUSE:
            ret = Param.map.mask_house
        elif where == Param.PLACE_YARD_BACK:
            ret = Param.map.mask_yard_back
        elif where == Param.PLACE_YARD_FRONT:
            ret = Param.map.mask_yard_front
        if ret is None:
            print("get_place_mask:", pos, Param.PLACE_TO_STR[where])
        return ret

    @classmethod
    def in_similar_place(cls, pos1, pos2):
        """
        Check 2 positions are in same place or not.
        """
        return cls.in_where(pos1) == cls.in_where(pos2)

    @classmethod
    def gen_random_pos(cls, map_array, avail_types, avail_pos=None):
        """
        Generate random position by types and specified mask.
        """
        mask_array = cls.gen_mask(map_array, avail_types, avail_pos)
        (width, height) = map_array.shape
        available_pos = []
        for i in range(width):
            for j in range(height):
                if mask_array[i][j]:
                    available_pos.append((i, j))
        if len(available_pos) > 0:
            index = random.randint(0, len(available_pos) - 1)
            return available_pos[index]
        else:
            print("No available positions")
            return None

    @classmethod
    def gen_next_positions(
        cls, map_array, avail_types, pos, max_step,
        avail_pos=None, remove_hist=None
    ):
        """
        Generate all next available positions.
        """
        step_mask = cls.gen_step_mask(map_array, pos, max_step)
        if avail_pos is not None:
            step_mask = step_mask & avail_pos
        mask_array = cls.gen_mask(map_array, avail_types, step_mask)
        np.copyto(Param.debug_array_2, mask_array)
        (width, height) = map_array.shape
        available_pos = []
        for i in range(width):
            for j in range(height):
                if mask_array[i][j]:
                    available_pos.append((i, j))
        if remove_hist:
            for hist in remove_hist:
                if len(avail_pos) > 2:
                    try:
                        available_pos.remove(hist)
                    except ValueError:
                        continue
        return available_pos

    @classmethod
    def select_near_pos(cls, available_pos, target):
        """
        Generate 1 nearest position from all next available positions.
        """
        min_dist = 100000
        ret_pos = None
        if available_pos:
            for pos in available_pos:
                if target is None:
                    raise PositionException("Target position is None")
                dist = cls.distance(pos, target)
                if min_dist > dist:
                    min_dist = dist
                    ret_pos = pos
        return ret_pos

    @classmethod
    def select_far_pos(cls, available_pos, target):
        """
        Generate 1 farest position from all next available positions.
        """
        max_dist = 0
        ret_pos = None
        if available_pos:
            for pos in available_pos:
                dist = cls.distance(pos, target)
                if max_dist < dist:
                    max_dist = dist
                    ret_pos = pos
        return ret_pos

    @classmethod
    def distance(cls, pos1, pos2, detour=True):
        """
        Calculate distance in 2 positions.
        Param detour is used to config detour or not.
        Because back yard and front yard should detour from house.
        """
        if detour:
            door_back = Param.map.door_back
            door_front = Param.map.door_front
            place1 = cls.in_where(pos1)
            place2 = cls.in_where(pos2)
            if place1 == place2:
                return cls.distance(pos1, pos2, False)
            elif (place1 == Param.PLACE_HOUSE
                    and place2 == Param.PLACE_YARD_BACK) or (
                place2 == Param.PLACE_HOUSE
                    and place1 == Param.PLACE_YARD_BACK
            ):
                return cls.distance(pos1, door_back, False) + cls.distance(
                    pos2, door_back, False
                )
            elif (place1 == Param.PLACE_HOUSE
                    and place2 == Param.PLACE_YARD_FRONT) or (
                place2 == Param.PLACE_HOUSE
                    and place1 == Param.PLACE_YARD_FRONT
            ):
                return cls.distance(pos1, door_front, False) + cls.distance(
                    pos2, door_front, False
                )
            elif (place1 == Param.PLACE_YARD_BACK
                  and place2 == Param.PLACE_YARD_FRONT):
                return (
                    cls.distance(pos1, door_back, False)
                    + cls.distance(pos2, door_front, False)
                    + cls.distance(door_back, door_front, False)
                )
            elif (place2 == Param.PLACE_YARD_BACK
                  and place1 == Param.PLACE_YARD_FRONT):
                return (
                    cls.distance(pos2, door_back, False)
                    + cls.distance(pos1, door_front, False)
                    + cls.distance(door_back, door_front, False)
                )
            else:
                print("uncovered place", place1, place2)
                return 1000000
        else:
            return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

    @classmethod
    def get_near_pos(cls, ori, new, target):
        """
        Difference which position is more close to target position.
        """
        if cls.distance(ori, target) >= cls.distance(new, target):
            return new
        return ori


class Map():
    """
    Define map to draw a figure contains grass, wall, garden,
    fence, house, road.
    """

    GRASS = 5
    WALL = 0
    GARDEN = 8
    FENCE_OUTSIDE = 2
    FENCE_INSIDE = 3
    HOUSE = 7
    ROAD = 10
    OUTSIDE_LAND = 4
    CMAP = "nipy_spectral"

    def __init__(self, config):
        self.size = config.get_map_size()
        (width, height) = config.get_map_size()
        self.width = width
        self.height = height
        array_data = np.full(shape=(width, height), fill_value=self.GRASS)
        self.array_data = array_data
        road_width = config.get_road_width()
        array_data[0:road_width, :] = self.ROAD
        array_data[width - road_width:width, :] = self.ROAD
        array_data[:, 0:road_width] = self.ROAD
        array_data[:, -road_width:] = self.ROAD
        wall_width = config.get_wall_width()
        distance = config.get_road_fence_dist()
        tmp_x = -road_width - distance
        array_data[tmp_x:-road_width, road_width:-road_width] = (
            self.OUTSIDE_LAND
        )
        tmp_x = road_width + wall_width
        array_data[road_width:tmp_x, road_width:-road_width] = (
            self.WALL
        )
        array_data[
            road_width:width - road_width - distance,
            road_width:road_width + wall_width,
        ] = self.WALL
        array_data[
            road_width:width - road_width - distance,
            -road_width - wall_width:-road_width,
        ] = self.WALL
        fence_width = config.get_fence_width()
        array_data[
            int(width / 2):int(width / 2) + fence_width,
            road_width + wall_width:-road_width - wall_width,
        ] = self.FENCE_INSIDE
        tmp_x = width - road_width - distance - fence_width
        array_data[
            tmp_x:width - road_width - distance,
            road_width + wall_width:-road_width - wall_width,
        ] = self.FENCE_OUTSIDE
        house_width, house_height = config.get_hourse_size()
        x = int((width - house_width) / 2)
        y = int((height - house_height) / 2)
        array_data[x:x + house_width, y:y + house_height] = self.HOUSE
        self.door_front = (x + house_width, y + int(house_height / 2))
        self.door_back = (x, y + int(house_height / 2))
        garden_width, garden_height = config.get_garden_size()
        x = y = wall_width + 10
        array_data[x:x + garden_width, y:y + garden_height] = self.GARDEN
        self.mask_grass = array_data == self.GRASS
        self.mask_garden = array_data == self.GARDEN
        self.mask_yard_front = np.array(self.mask_grass)
        self.mask_yard_front[: int(width / 2), :] = False
        self.mask_yard_back = np.array(self.mask_grass)
        self.mask_yard_back[int(width / 2):, :] = False
        self.mask_yard_back = self.mask_yard_back | self.mask_garden
        self.mask_house = array_data == self.HOUSE
        self.available_area = (
            self.mask_house | self.mask_yard_back | self.mask_yard_front
        )

    def plot(self, ax):
        ax.imshow(self.array_data, cmap=Map.CMAP)
