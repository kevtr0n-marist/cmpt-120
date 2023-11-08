import json
from datetime import datetime


class Event:
    '''
    This class serves as the superclass for all events.
    '''

    def __init__(self):
        self.event_data = {}

    def __str__(self) -> str:
        return json.dumps(self.event_data, sort_keys=False, indent=2)


class InventoryAddEvent(Event):
    '''
    This class serves as an event for when something was added into the inventory.
    '''

    def __init__(self, added):
        self.event_data = {
            "added": added,
            "timestamp": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        }


class InventoryRemoveEvent(Event):
    '''
    This class serves as an event for when something was removed from the inventory.
    '''

    def __init__(self, removed):
        self.event_data = {
            "removed": removed,
            "timestamp": datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        }
