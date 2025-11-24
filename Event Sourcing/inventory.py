from event import Event,EventType
from event_store import EventStore

class Inventory:
    def __init__(self, store: EventStore)-> None :
        self.store = store

    def add_item(self,item: str) -> None :
        event = Event(type=EventType.ITEM_ADDED,data=item)
        self.store.append(event)