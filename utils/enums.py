from enum import Enum

class PaleState(Enum):
    NONE = 0
    DISTANT = 1
    CLOSE = 2
    CLEAR = 3

class LightState(Enum):
    DUSK = 1
    TWILIGHT = 2
    NIGHT = 3
    DAYLIGHT = 4

class SouthState(Enum):
    HIDDEN = 0
    VISIBLE = 1
    LOCKED = 2

class EndingState(Enum):
    CLIFF = 0
    TRUCK = 1
    TRAPPED = 2
    ESCAPED = 3