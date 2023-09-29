# class Person():
#     def __init__(self):  # List of attributes
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#
#     def info(self):
#         print(f'Name: {self.name} Age: {self.age} Gender: {self.gender}')
#
# class Employee(Person):  # Employee inherited from Person
#     def __init__(self):
#
#         self.emp_id = ""
#         self.position = ""
#
#         def info(self):
#             print(f'Name: {self.name} '
#                   f'Age: {self.age} '
#                   f'Gender: {self.gender}'
#                   f'EMP_ID: {self.emp_id}'
#                   f'Position: {self.position}')
#
#
#
# p1 = Person()
# p1.name = "Aphisada Suksom"
# p1.age = 20
# p1.gender = "Male"
#
# emp1 = Employee()
# emp1.name = "Aphisada Suksom"
# emp1.age = 21
# emp1.gender = "Male"
# emp1.emp_id = "EMP006"
# emp1.position = "Lecturer"
#
# p1.info()
# emp1.info()
#
# lst = [p1,emp1]
#
# for obj in lst:
#     print(obj.__class__.__name__, end="")
#     obj.info()

class Person1():
    def __init__(self):  # List of attributes
        self.name = ""
        self.age = 0
        self.gender = ""

    def info(self):
        print(f'Name: {self.name} '
              f'Age: {self.age} '
              f'Gender: {self.gender}')

class student(Person1):
    def __init__(self):
        self.student_id = 0
        self.major = ""
        self.university = ""

    def info(self):
        print(f'Name: {self.name} '
              f'Age: {self.age} '
              f'Gender: {self.gender}'
              f'Student_ID: {self.student_id}'
              f'Major: {self.major}'
              f'University: {self.university}')

std = student()
std.name = "Aphisada Suksom"
std.age = 20
std.gender = "Male"
std.student_id = 36441760006
std.major = "MIT431"
std.university = "Rajamangala University of Technology Srivijaya"

std.info()

lst = [std]

for obj in lst:
    print(obj.__class__.__name__, end="")
    obj.info()
