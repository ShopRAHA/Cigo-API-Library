from enum import Enum


class ActionStatus(Enum):
    undetermined = 'undetermined'
    completed = 'completed'
    incomplete = 'incomplete'
    damaged = 'damaged'
