

# class Person :
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def display (self):
#         print(f"{self.name} is {self.age} years old weighs {self.weight}kg")
#
# jane = Person("Jane Smith", 35, 2500)
# Damian = Person("Damian Smith", 35, 2500)
#
#
# jane.display()
# Damian.display()

#TASK


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

student1 = Student("Alice", 20, "Computer Science")
student2 = Student("Bob", 22, "Cybersecurity")

student1.display_details()
student2.display_details()