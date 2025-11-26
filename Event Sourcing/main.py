from event_store import EventStore
from inventory import Inventory

def main() -> None:
    store = EventStore()
    inventory = Inventory(store)

    inventory.add_item("Heorot")
    inventory.add_item("Beowulf")
    inventory.add_item("Hrothgar")
    inventory.add_item("Dernhelm")
    inventory.add_item("Unferth")

    items = inventory.get_items()
    for item, count in items:
        print(f"{item}: {count}")

    print(f"Count of Beowulf: {inventory.get_count('Beowulf')}")
    print(f"Count of non-existent Ecgtheow: {inventory.get_count('Ecgtheow')}")

if __name__ == "__main__":
    main()