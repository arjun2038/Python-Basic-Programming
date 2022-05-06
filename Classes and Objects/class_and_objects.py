#Creating Classes
class Student:
    no_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.no_of_students += 1

    def displayStudent(self):
        print("Name:", self.name, "Age:", self.age)

    def displayNumberOfStudents(self):
        print("No of Students:", self.no_of_students)

#Creating Instance Objects
student1 = Student("Arjun", 22)
student2=Student("Nihal",24)

#Accessing Attributes
student1.displayStudent()
student2.displayStudent()
student2.displayNumberOfStudents()
print(hasattr(student1,"name"))
print(getattr(student1,"name"))
setattr(student1,"name","Aswin")
student1.displayStudent()
delattr(student1,"name")

#Built-In Class Attributes
print(Student.__dict__)
print(Student.__name__)
print(Student.__module__)
print(Student.__doc__)

