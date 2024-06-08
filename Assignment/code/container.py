"""
container.py - maintain status and handle flow

Written by : Ben Niu
Student ID : 21678145

Includes:
    Container

Versions:
    - implement time by Ben Niu 03/05/24
    - implement control flow by Ben Niu 02/05/24
    - initial version by Ben Niu 26/04/24
"""

import numpy as np

from animals import Animal, Dog, Puppy, Squirrel
from common import Map, Param
from humans import Human, Owner, Friend, Stranger, Intruder
from things import Ball, Door, Swing, Water


class Container():
    """
    Define Container class.

    This class is used to maintain all items, like creatures,
    humans, map, config, time counter.
    """

    @classmethod
    def init_obj(cls, config):
        # Init all objects
        Param.config = config
        Param.pause = False
        Param.curr_time = config.get_start_time()
        Param.time_table = cls.init_timetable()
        Param.time_sec = cls.get_time_sec(cls.get_hour())
        Param.map = Map(config)
        Param.posi_record = np.full(
            (Param.map.width, Param.map.height),
            fill_value=Param.POSI_AVAILABLE
        )
        Param.posi_history = np.zeros((Param.map.width, Param.map.height))
        Param.debug_array = np.full((Param.map.width, Param.map.height),
                                    fill_value=0, dtype=float)
        Param.debug_array_2 = np.full((Param.map.width, Param.map.height),
                                      fill_value=0, dtype=float)
        Param.doors = []
        Param.humans = []
        Param.dogs = []
        Param.puppies = []
        Param.squirrels = []
        Param.waters = []
        Param.toys = []
        Param.foods = []
        Param.all_objs = [
            Param.doors,
            Param.humans,
            Param.dogs,
            Param.puppies,
            Param.squirrels,
            Param.waters,
            Param.toys,
            Param.foods,
        ]
        Param.doors.extend(cls.build_doors(config))
        Param.humans.extend(cls.build_humans(config))
        dogs, puppies = cls.build_dogs(config)
        Param.dogs.extend(dogs)
        Param.puppies.extend(puppies)
        Param.squirrels.extend(cls.build_squirrels(config))
        Param.waters.extend(cls.build_waters(config))
        Param.toys.extend(cls.build_toys(config))

    @classmethod
    def init_timetable(cls):
        # Init timetable in one day.
        time_table = []
        time_table.extend([Param.TIME_SEC_SLEEP] * 8)
        time_table.extend([Param.TIME_SEC_EAT] * 2)
        time_table.extend([Param.TIME_SEC_PLAY] * 5)
        time_table.extend([Param.TIME_SEC_EAT] * 2)
        time_table.extend([Param.TIME_SEC_PLAY] * 5)
        time_table.extend([Param.TIME_SEC_SLEEP] * 2)
        return time_table

    @classmethod
    def init_stat(cls):
        # Init the status of all objects.
        for door in Param.doors:
            if door.type == Door.TYPE_FRONT:
                door.position = Param.map.door_front
            elif door.type == Door.TYPE_BACK:
                door.position = Param.map.door_back
        for item in Param.humans:
            if isinstance(item, Owner) or isinstance(item, Friend):
                pos = cls.get_random_position(item, Map.HOUSE)
                item.position = pos
            if isinstance(item, Stranger) or isinstance(item, Intruder):
                pos = cls.get_random_position(item, Map.ROAD)
                item.position = pos
        for item in Param.dogs:
            pos = cls.get_random_position(item, Map.HOUSE)
            item.position = pos
        for item in Param.puppies:
            pos = cls.get_random_position(item, Map.HOUSE)
            item.position = pos
        for item in Param.squirrels:
            pos = cls.get_random_position(item, Map.GRASS)
            item.position = pos
        for item in Param.waters:
            pos = cls.get_random_position(item, Map.GARDEN)
            item.position = pos
        for item in Param.toys:
            pos = cls.get_random_position(item, Map.GRASS)
            item.position = pos

    @classmethod
    def get_random_position(cls, item, types):
        pos = item.gen_random_pos(
            Param.map.array_data, types,
            Param.posi_record == Param.POSI_AVAILABLE
        )
        if pos:
            Param.posi_record[pos] = Param.POSI_UNAVAILABLE
        return pos

    @classmethod
    def plot_map(cls, ax):
        Param.map.plot(ax)

    @classmethod
    def plot_obj(cls, ax):
        for items in Param.all_objs:
            for item in items:
                item.plot(ax)

    @classmethod
    def build_doors(cls, config):
        doors = []
        doors.append(Door("D", Door.TYPE_FRONT))
        doors.append(Door("D", Door.TYPE_BACK))
        return doors

    @classmethod
    def build_humans(cls, config):
        humans = []
        num = config.get_simu_owner()
        for i in range(num):
            humans.append(Owner(f"O{i}"))
        num = config.get_simu_friend()
        for i in range(num):
            humans.append(Friend(f"F{i}"))
        num = config.get_simu_stranger()
        for i in range(num):
            humans.append(Stranger(f"S{i}"))
        num = config.get_simu_intruder()
        for i in range(num):
            humans.append(Intruder(f"I{i}"))
        return humans

    @classmethod
    def build_dogs(cls, config):
        dogs = []
        puppies = []
        num_d = config.get_simu_dog()
        num_p = config.get_simu_puppy()
        colours = config.get_simu_dog_colours()
        for i in range(num_d):
            dogs.append(Dog(f"D{i}", colours[i % len(colours)]))
        for i in range(num_p):
            dogs.append(Puppy(f"P{i}", colours[i % len(colours)]))
        return (dogs, puppies)

    @classmethod
    def build_squirrels(cls, config):
        squs = []
        num = config.get_simu_squirrel()
        for i in range(num):
            squs.append(Squirrel(f"S{i}"))
        return squs

    @classmethod
    def build_waters(cls, config):
        waters = []
        num = config.get_simu_water()
        for i in range(num):
            waters.append(Water(f"W{i}"))
        return waters

    @classmethod
    def build_toys(cls, config):
        toys = []
        num = config.get_simu_swing()
        for i in range(num):
            toys.append(Swing(f"S{i}"))
        num = config.get_simu_ball()
        colours = config.get_simu_ball_colours()
        for i in range(num):
            toys.append(Ball(f"B{i}", colours[i % len(colours)]))
        return toys

    @classmethod
    def get_title(cls):
        (y, m, d), (h, mi, s) = cls.get_ymd_hms()
        return "Time - %02d:%02d:%02d - %s" % (
            h,
            mi,
            s,
            Param.TIME_SECS[cls.get_time_sec(h)],
        )

    @classmethod
    def get_ymd_hms(cls):
        # Get year, month, day, hour, minute, second from current time.
        curr_time = Param.curr_time
        year = curr_time // Param.YEAR
        curr_time -= year * Param.YEAR
        month = curr_time // Param.MONTH
        curr_time -= month * Param.MONTH
        day = curr_time // Param.DAY
        curr_time -= day * Param.DAY
        hour = curr_time // Param.HOUR
        curr_time -= hour * Param.HOUR
        minu = curr_time // Param.MINUTE
        curr_time -= minu * Param.MINUTE
        sec = curr_time
        return (year, month, day), (hour, minu, sec)

    @classmethod
    def get_hour(cls):
        (year, month, day), (hour, minu, sec) = cls.get_ymd_hms()
        return hour

    @classmethod
    def pause(cls):
        # Pause time and simulation.
        Param.pause = not Param.pause

    @classmethod
    def is_paused(cls):
        return Param.pause

    @classmethod
    def second(cls):
        # callback method when per second passed.
        if Param.pause:
            return
        Param.curr_time += 1
        Param.time_sec = cls.get_time_sec(cls.get_hour())
        for items in Param.all_objs:
            for item in items:
                item.next_step()
                # Param.posi_record[item.position] = Param.POSI_UNAVAILABLE
                # for i, pos in enumerate(item.get_history_pos()):
                #     Param.posi_record[pos] = i+1+Param.POSI_MOCK
                # if item.target is not None:
                #     if isinstance(item, Animal):
                #         Param.posi_record[item.target] = Param.POSI_MOCK
        foods = Param.foods
        for food in foods:
            Param.posi_record[food.position] = Param.POSI_UNAVAILABLE
            if food.is_eat_up():
                Param.posi_record[food.position] = Param.POSI_AVAILABLE
                Param.foods.remove(food)
        Param.posi_history.fill(0)
        for items in Param.all_objs:
            for item in items:
                for i, pos in enumerate(item.get_history_pos()):
                    Param.posi_history[pos] = i + 1
                if item.target is not None:
                    if isinstance(item, Animal):
                        Param.posi_history[item.target] \
                            = Param.posi_history.max()
                    elif isinstance(item, Human):
                        if isinstance(item.target, tuple):
                            Param.posi_history[item.target] \
                                = Param.posi_history.max()

    @classmethod
    def time_fly(cls, sec):
        # Change time with delta second.
        old_time = Param.curr_time
        Param.curr_time += sec
        for items in Param.all_objs:
            for item in items:
                item.time_changed(old_time, Param.curr_time, sec)

    @classmethod
    def get_time_sec(cls, hour):
        # Get time section by hour.
        return Param.time_table[hour]
