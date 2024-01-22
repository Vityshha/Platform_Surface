import enum

class State_scenario(enum.Enum):
    CONTROL_BY_SURFACE = 0
    INFINITY = 1
    CIRCLE = 2
    FOLLOWING_TARGET = 3
    TRAJECTORY = 4
    FOLLOWING_HUMAN = 5
