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
        for event in self.store.get_all_events():
            if event.type == EventType.ITEM_ADDED:
                counts[event.data] += 1
            elif event.type == EventType.ITEM_REMOVED:
                counts[event.data] -= 1

        return [
            (item, count) for item, count in counts.items() if count > 0
        ]
        
    def get_count(self, item:str) -> int :
        return dict(self.get_items()).get(item,0)