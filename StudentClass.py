class Student:
    def __init__ (self, name, grade):
        self.name = name
        self.grade = grade
    
    def introduce(self):
        print("Hi, my name is ", self.name, " and I am in grade ", self.grade)
    
student1 = Student("John", 12)
student2 = Student("Maria", 10)

student1.introduce()
student2.introduce()
