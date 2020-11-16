from enum import Enum


class MoveStatus(Enum):
    INVALID_MOVE = -1
    VALID_MOVE = 0
    EZ_KILL = 1
