import pytest
from event import *
from demo import *
from event_listener import EventListener

class MyListener(EventListener):

    def __init__(self):
        self.received_event = False

    def handle_event(self, event):
        if isinstance(event, Event):
            self.received_event = True

listener = MyListener()

@pytest.fixture(autouse=True)
def setup_and_teardown():
    global listener
    listener.received_event = False
    yield
    # teardown

class TestClass:

    def test_received(self):
        '''
        Assert that the event is received when it is registered.
        '''

        # create our class.
        course = Course("CMPT120")

        # add our listener.
        course.add_listener(listener)
        
        # create our student.
        student = Student("Jane", "Smith")

        # add student to course.
        course.add_student(student)

        assert listener.received_event

    def test_not_received(self):
        '''
        Assert that the event is not received if it was not registered.
        '''
        
        # create our class.
        course = Course("CMPT120")

        # don't add our listener.
        # course.add_listener(listener)
        
        # create our student.
        student = Student("Jane", "Smith")

        # add student to course.
        course.add_student(student)

        assert not listener.received_event
