class Student:
    def __init__(self):
        self.grade = None

    def view_grade(self):
        return self.grade


class Teacher:
    def assign_grade(self, student, grade):
        student.grade = grade
