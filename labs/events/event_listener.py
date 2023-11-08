from event import Event

class EventListener(object):
    '''
    This class holds a method that subclasses must implement.
    '''

    def handle_event(self, event):
        '''
        When this the subclass is registered as an event listener the handler will notify this
        class by invoking this method.
        '''
        if isinstance(event, Event):
            raise TypeError("'event' must be of type Event.")
        pass