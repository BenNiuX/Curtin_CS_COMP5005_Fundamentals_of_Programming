"""
snoo.py - base simulation for the FOP Assignment, Sem 1 2024

Written by : Ben Niu
Student ID : 21678145

Usage:
    snoo.py [-h] [-f CONFIG] [-s SPEED]
    optional arguments:
        -h, --help            show this help message and exit
        -f CONFIG, --config CONFIG
                                specify config file to program
        -s SPEED, --speed SPEED
                                specify simulation speed

Versions:
    - implement time and argument parsing by Ben Niu 03/05/24
    - implement control flow by Ben Niu 02/05/24
    - initial by Ben Niu 26/04/24
"""


import argparse
import time
from matplotlib import pyplot as plt
from matplotlib.widgets import Button
from common import Param
from config import Config
from container import Container
from exceptions import ConfigException


def time_passed_hour(event):
    # Time change function: 1 hour passed.
    Container.time_fly(Param.HOUR)


def time_passed_min(event):
    # Time change function: 1 minute passed.
    Container.time_fly(Param.MINUTE)


def exit_fun(event):
    # Exit function callback.
    exit()


def pause_fun(event):
    # Pause function callback.
    Container.pause()


def main(config):
    # Init all objects and their status.
    Container.init_obj(config)
    Container.init_stat()
    # Calculate sleep to control simulate speed.
    speed = 1.0 / config.get_speed()

    plt.ion()
    fig, axs = plt.subplots(
        nrows=1, ncols=5, figsize=config.get_figsize()
    )

    manager = plt.get_current_fig_manager()
    manager.set_window_title("Simulation")
    manager.full_screen_toggle()

    # Init control buttons.
    hour_passed = fig.add_axes([0.2, 0.1, 0.09, 0.05])
    min_passed = fig.add_axes([0.3, 0.1, 0.09, 0.05])
    pause = fig.add_axes([0.4, 0.1, 0.09, 0.05])
    exit = fig.add_axes([0.5, 0.1, 0.09, 0.05])
    btn_add_hour = Button(hour_passed, '1 hour passed')
    btn_add_min = Button(min_passed, '1 min passed')
    btn_pause = Button(pause, 'Pause/Resume')
    btn_exit = Button(exit, 'EXIT')
    btn_add_hour.on_clicked(time_passed_hour)
    btn_add_min.on_clicked(time_passed_min)
    btn_exit.on_clicked(exit_fun)
    btn_pause.on_clicked(pause_fun)

    titles = [Container.get_title(), "Position", "History", "Sense", "Mask"]
    arrays = [None, Param.posi_record, Param.posi_history, Param.debug_array,
              Param.debug_array_2]
    cmaps = [None, "hot", "gray", "hot", "hot"]

    for i in range(config.get_simu_num()):
        time_start = time.time()
        Container.second()
        for i, ax in enumerate(axs):
            if i == 0:
                ax.set_title(Container.get_title())
                Container.plot_map(ax)
                Container.plot_obj(ax)
            else:
                ax.set_title(titles[i])
                ax.imshow(arrays[i], cmaps[i])
        fig.canvas.draw()
        fig.canvas.flush_events()
        for ax in axs:
            ax.clear()
        # Container.second()
        time_end = time.time()
        time_consumed = time_end - time_start
        if time_consumed < speed:
            time.sleep(speed - time_consumed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog=__file__,
        description="Base simulation for the FOP Assignment, Sem 1 2024",
        epilog="Author: Ben Niu, Version: 1.0.0",
    )
    parser.add_argument('-f', '--config', default=Config.DEFAULT_CONFIG_FILE,
                        help="specify config file to the program: config.cfg")
    parser.add_argument('-s', '--speed', type=int,
                        default=Config.DEFAULT_SPEED,
                        help="specify simulation speed: 1 for 1s, 5 for 0.2s")
    args = parser.parse_args()
    try:
        config = Config(args.config)
        config.set_speed(args.speed)
        main(config)
    except ConfigException as e:
        # Handle config error.
        print(e)
        parser.print_help()
