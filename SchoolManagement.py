class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class School:
    def __init__(self):
        self.students = []  # list of Student objects

    def add_student(self, student):
        # Check for duplicate student IDs
        for s in self.students:
            if s.student_id == student.student_id:
                print("Error: Student ID already exists.")
                return
        self.students.append(student)

    def remove_student(self, name):
        for s in self.students:
            if s.name == name:
                self.students.remove(s)
                return
        print("Student not found.")

    def list_students(self):
        for s in self.students:
            print(f"Name: {s.name}, ID: {s.student_id}")
