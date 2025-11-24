from event import Event,EventType
from event_store import EventStore

from collections import Counter

class Inventory:
    def __init__(self, store: EventStore)-> None :
        self.store = store

    def add_item(self,item: str) -> None :
        event = Event(type=EventType.ITEM_ADDED,data=item)
        self.store.append(event)

    def get_items(self) -> list[tuple[str, int]] :
        counts = Counter[str]()
        for event in self.store.get_events():
            if event.type == EventType.ITEM_ADDED:
                counts[event.data] += 1
        return list(counts.items())