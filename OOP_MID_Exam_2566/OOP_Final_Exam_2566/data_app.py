from oppmodel import Person, Student, Employee, Tablet, Laptop, Mobile

def display_option():

    print("User Data")
    print("\n-------------------------------")
    print("1.Add user (Person)")
    print("2.Add user (Student)")
    print("3.Add user (Employee)")
    print("4.exit")
    print("-------------------------------\n")
    select = int(input("select (1-4)?: "))

    if select == 1:
        input_person_data()
    elif select == 2:
        input_student_data()
    elif select == 3:
        input_employee_data()
    elif select == 4:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, select number 1-5")

def input_person_data():
    name = input("Enter person name : ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    Person.my_person.append(Person(name,age,email))
    print("\n-------------------------------")
    print("The data has been saved.")
    print("-------------------------------\n")

def input_student_data():
    sid = input("Enter student id: ")
    name = input("Enter student name: ")
    major = input("Enter major: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    Student.my_student.append(Student(sid, name, age, major, email))
    print("\n-------------------------------")
    print("The data has been saved.")
    print("-------------------------------\n")

def input_employee_data():
    eid = input("Enter employee id: ")
    name = input("Enter employee: ")
    position = input("Enter position: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    Employee.my_employee.append(Employee(eid,name,position,age,email))
    print("\n-------------------------------")
    print("The data has been saved.")
    print("-------------------------------\n")

s = 0
while s == 0:
    display_option()