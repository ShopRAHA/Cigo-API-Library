from enum import Enum


class JobStatus(Enum):
    staging = 'staging'
    new = 'new'
    in_progress = 'in progress'
    completed = 'completed'
    incomplete = 'incomplete'
    partially_completed = 'partially completed'
    damaged = 'damaged'
    resolved = 'resolved'
