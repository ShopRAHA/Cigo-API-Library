from enum import Enum


class JobActionType(Enum):
    delivery = 'delivery'
    return_job = 'return'
    pickup = "pickup"
    installation = "installation"
    service = "service"
    exchange = "exchange"
