import threading

from event import Event
from event_listener import EventListener

class EventHandler(object):
    '''
    Subclasses of this class are able to add/remove listeners and asynchronously notify
    them of any worthwhile events.
    '''
    
    def __init__(self):
        self.listeners = []

    def add_listener(self, listener):
        '''
        Registers an EventListener for notifications.
        '''
        if isinstance(listener, EventListener):
            self.listeners.append(listener)

    def remove_listener(self, listener):
        '''
        Unregisters an EventListener for notifications.
        '''
        if listener in self.listeners:
            self.listeners.remove(listener)
    
    def notify_listeners(self, event):
        '''
        Sends an event to all registered EventListeners.
        '''
        if not isinstance(event, Event):
            raise TypeError("'event' must be of type Event.")
        for listener in self.listeners:
            # asynchronously notify each listener in separate threads.
            t = threading.Thread(target=listener.handle_event, args=(event,))
            t.start()
