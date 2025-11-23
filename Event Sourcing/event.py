# Stop Overwriting State And Use Event Sourcing Instead
# https://youtu.be/t-LC1dWLpNs?si=5DNFJqSoUokAKper

from enum import StrEnum
from dataclasses import dataclass
from datetime import datetime

class EventType(StrEnum):
    ITEM_ADDED = "item_added"
    ITEM_REMOVED = "item_removed"

@dataclass(frozen=True)
class Event:
    type : EventType
    data : str
    timestamp : datetime = field(default_factory=datetime.now)

