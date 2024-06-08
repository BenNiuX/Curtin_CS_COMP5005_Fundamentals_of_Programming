"""
exceptions.py - define exception classes

Written by : Ben Niu
Student ID : 21678145

Includes:
    ConfigException
    PositionException

Versions:
    - define ConfigException and PositionException by Ben Niu 26/04/24
    - initial version by Ben Niu 26/04/24
"""


class ConfigException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"


class PositionException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"{self.message}"
