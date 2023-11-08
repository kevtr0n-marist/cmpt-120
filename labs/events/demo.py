import uuid
import json

from event import InventoryAddEvent, InventoryRemoveEvent
from event_handler import EventHandler
from event_listener import EventListener


class CourseAddEvent(InventoryAddEvent):
    '''
    A custom event to be sent when a student is registered to a class.
    '''
    
    def __init__(self, added, credits):
        super().__init__(added)
        self.event_data["credits"] = credits

class CourseRemoveEvent(InventoryRemoveEvent):
    '''
    A custom event to be sent when a student is unregistered from a class.
    '''

    def __init__(self, removed, credits):
        super().__init__(removed)
        self.event_data["credits"] = credits


class Student(EventListener):

    def __init__(self, first_name, last_name):
        self.uuid = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}.{last_name.lower()}@marist.edu"
        self.credits = 0

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Student):
            return other.email == self.email or other.uuid == self.uuid
        return False
    
    def __hash__(self) -> int:
        return hash(self.email)
    
    def __str__(self) -> str:
        return json.dumps(dict(self), indent=2, sort_keys=False, ensure_ascii=False)
    
    def handle_event(self, event):
        '''
        The student's 'credits' property is updated via events.
        '''
        if isinstance(event, CourseAddEvent):
            self.credits += event.event_data["credits"]
        elif isinstance(event, CourseRemoveEvent):
            self.credits -= event.event_data["credits"]


class Teacher(EventListener):

    def __init__(self, first_name, last_name):
        self.uuid = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name.lower()}.{last_name.lower()}@marist.edu"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Student):
            return other.email == self.email or other.uuid == self.uuid
        return False
    
    def __hash__(self) -> int:
        return hash(self.email)
    
    def handle_event(self, event):
        print(f"'{self.email}' received course registration event: {event}")


class Course(EventHandler):
    
    def __init__(self, course_id, credits, teacher=None):
        super().__init__()
        self.course_id = course_id
        self.credits = credits
        if isinstance(teacher, Teacher):
            self.teacher = teacher
            self.add_listener(teacher)
        self.students = []
    
    def add_student(self, student):
        # ensure 'student' is a Student object.
        if not isinstance(student, Student):
            raise TypeError("'student' must be a Student.")
        # ensure 'student' isn't already registered.
        if student in self.students:
            raise ValueError(f"Student with email '{student.email}' already registered to course {self.course_id}.")
        # add student to course list.
        self.students.append(student)
        # add student as listener.
        self.listeners.append(student)
        # create course add event.
        event = CourseAddEvent(student.__dict__, self.credits)
        # notify everyone who is interested.
        self.notify_listeners(event)

    def remove_student(self, student):
        # ensure 'student' is a Student object.
        if not isinstance(student, Student):
            raise TypeError("'student' must be a Student.")
        # ensure 'student' is registered.
        if student not in self.students:
            raise ValueError(f"Student with email '{student.email}' is not registered to course {self.course_id}.")
        # remove student from class
        self.students.remove(student)
        # create course remove event.
        event = CourseRemoveEvent(student.__dict__, self.credits)
        # notify everyone who is interested.
        self.notify_listeners(event)
        # remove the student as a listener after event is sent.
        self.remove_listener(student)


def main():
    # create teacher
    teacher = Teacher("Kevin", "Hayden")

    # create course for teacher to teach
    course = Course("CMPT120", 4, teacher)

    # create student to add to course
    student = Student("Alice", "Smith")

    # register the student
    course.add_student(student)

    # unregister the student
    course.remove_student(student)

    print("Removing listener...")
    print("Note that there aren't any event notifications after this.")

    # remove the listener
    course.remove_listener(teacher)

    # register the students
    course.add_student(student)

    # unregister the students
    course.remove_student(student)

if __name__ == '__main__':
    main()
