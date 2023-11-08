import uuid
import json

from event import InventoryAddEvent, InventoryRemoveEvent
from event_handler import EventHandler
from event_listener import EventListener

class Student:

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
    
    def __str__(self) -> str:
        return json.dumps(dict(self), indent=2, sort_keys=False, ensure_ascii=False)


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
    
    def __init__(self, course_id, teacher=None):
        super().__init__()
        self.course_id = course_id
        if isinstance(teacher, Teacher):
            self.teacher = teacher
            self.add_listener(teacher)
        self.students = []
    
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("'student' must be a Student.")
        if student in self.students:
            raise ValueError(f"Student with email '{student.email}' already registered to course {self.course_id}.")
        self.students.append(student)
        event = InventoryAddEvent(student.__dict__)
        self.notify_listeners(event)

    def remove_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("'student' must be a Student.")
        if student not in self.students:
            raise ValueError(f"Student with email '{student.email}' is not registered to course {self.course_id}.")
        self.students.remove(student)
        event = InventoryRemoveEvent(student.__dict__)
        self.notify_listeners(event)


def main():
    # create teacher
    teacher = Teacher("Kevin", "Hayden")

    # create course for teacher to teach
    course = Course("CMPT120", teacher)

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
