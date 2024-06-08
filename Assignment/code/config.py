"""
config.py - maintain configuration

Written by : Ben Niu
Student ID : 21678145

Includes:
    Config

Versions:
    - implement details by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import configparser
import os

from exceptions import ConfigException


class Config():
    """
    Define Configuration class.

    This class is used to read *.cfg file and provide API for other modules.
    """
    myclass = "Config"

    DEFAULT_CONFIG_FILE = "config_def.cfg"
    DEFAULT_SPEED = 5

    SECTION_DEF = "DEFAULT"
    DEF_FIG_WIDTH = "fig_width"
    DEF_FIG_HEIGHT = "fig_height"
    DEF_SPEED = "speed"

    SECTION_MAP = "MAP"
    MAP_SIZE_WIDTH = "size_width"
    MAP_SIZE_HEIGHT = "size_height"
    MAP_HOUSE_WIDTH = "house_width"
    MAP_HOURSE_HEIGHT = "hourse_height"
    MAP_GARDEN_WIDTH = "garden_width"
    MAP_GARDEN_HEIGHT = "garden_height"
    MAP_ROAD_WIDTH = "road_width"
    MAP_WALL_WIDTH = "wall_width"
    MAP_FENCE_WIDTH = "fence_width"
    MAP_ROAD_FENCE_DISTANCE = "road_fence_distance"

    SECTION_SIMU = "SIMULATION"
    SIMU_NUM = "simu_num"
    SIMU_START = "simu_start"
    SIMU_DOG = "simu_dog"
    SIMU_PUPPY = "simu_puppy"
    SIMU_DOG_COLOURS = "simu_dog_colours"
    SIMU_SQUIRREL = "simu_squirrel"
    SIMU_OWNER = "simu_owner"
    SIMU_FRIEND = "simu_friend"
    SIMU_STRANGER = "simu_stranger"
    SIMU_INTRUDER = "simu_intruder"
    SIMU_WATER = "simu_water"
    SIMU_SWING = "simu_swing"
    SIMU_BALL = "simu_ball"
    SIMU_BALL_COLOURS = "simu_ball_colours"

    def __init__(self, config_file=None):
        self.config_file = config_file
        self.configs = self.parse_cfg()

    def get_cfg_file(self):
        if not self.config_file:
            self.config_file = self.DEFAULT_CONFIG_FILE
        return self.config_file

    def get_cfg(self):
        return self.configs

    def parse_cfg(self):
        cfg_file = self.get_cfg_file()
        if not os.path.exists(cfg_file):
            raise ConfigException(f"Config file: {cfg_file} not exists")
        config = configparser.ConfigParser()
        config.read(cfg_file, encoding="utf-8")
        return config

    def get_figsize(self):
        return (
            self.configs.getint(self.SECTION_DEF, self.DEF_FIG_WIDTH,
                                fallback=10),
            self.configs.getint(self.SECTION_DEF, self.DEF_FIG_HEIGHT,
                                fallback=15),
        )

    def get_speed(self):
        return (
            self.configs.getint(self.SECTION_DEF, self.DEF_SPEED,
                                fallback=self.DEFAULT_SPEED)
        )

    def set_speed(self, speed):
        self.configs.set(self.SECTION_DEF, self.DEF_SPEED, str(speed))

    def get_map_size(self):
        return (
            self.configs.getint(self.SECTION_MAP, self.MAP_SIZE_WIDTH,
                                fallback=10),
            self.configs.getint(self.SECTION_MAP, self.MAP_SIZE_HEIGHT,
                                fallback=15),
        )

    def get_hourse_size(self):
        return (
            self.configs.getint(self.SECTION_MAP, self.MAP_HOUSE_WIDTH,
                                fallback=120),
            self.configs.getint(self.SECTION_MAP, self.MAP_HOURSE_HEIGHT,
                                fallback=90),
        )

    def get_garden_size(self):
        return (
            self.configs.getint(self.SECTION_MAP, self.MAP_GARDEN_WIDTH,
                                fallback=20),
            self.configs.getint(self.SECTION_MAP, self.MAP_GARDEN_HEIGHT,
                                fallback=15),
        )

    def get_road_width(self):
        return self.configs.getint(self.SECTION_MAP, self.MAP_ROAD_WIDTH,
                                   fallback=5)

    def get_wall_width(self):
        return self.configs.getint(self.SECTION_MAP, self.MAP_WALL_WIDTH,
                                   fallback=1)

    def get_fence_width(self):
        return self.configs.getint(self.SECTION_MAP, self.MAP_FENCE_WIDTH,
                                   fallback=1)

    def get_road_fence_dist(self):
        return self.configs.getint(
            self.SECTION_MAP, self.MAP_ROAD_FENCE_DISTANCE, fallback=10
        )

    def get_simu_num(self):
        return eval(self.configs.get(self.SECTION_SIMU, self.SIMU_NUM,
                                     fallback="100"))

    def get_start_time(self):
        return eval(self.configs.get(self.SECTION_SIMU, self.SIMU_START,
                                     fallback="0"))

    def get_simu_dog(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_DOG,
                                   fallback=0)

    def get_simu_puppy(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_PUPPY,
                                   fallback=0)

    def get_simu_dog_colours(self):
        return eval(
            self.configs.get(
                self.SECTION_SIMU, self.SIMU_DOG_COLOURS,
                fallback="[\"black\"]")
            )

    def get_simu_squirrel(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_SQUIRREL,
                                   fallback=0)

    def get_simu_owner(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_OWNER,
                                   fallback=0)

    def get_simu_friend(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_FRIEND,
                                   fallback=0)

    def get_simu_stranger(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_STRANGER,
                                   fallback=0)

    def get_simu_intruder(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_INTRUDER,
                                   fallback=0)

    def get_simu_water(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_WATER,
                                   fallback=0)

    def get_simu_swing(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_SWING,
                                   fallback=0)

    def get_simu_ball(self):
        return self.configs.getint(self.SECTION_SIMU, self.SIMU_BALL,
                                   fallback=0)

    def get_simu_ball_colours(self):
        return eval(
            self.configs.get(
                self.SECTION_SIMU, self.SIMU_BALL_COLOURS,
                fallback="[\"pink\"]")
            )
