
class Person:
    my_person = []
    def __str__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email

    def info(self):
        print(f'\tPerson Name:         {self.name} \n' 
              f'\tAge:                 {self.age} \n' 
              f'\tEmail:               {self.email} \n')

class Student:
    my_student = []
    def __str__(self,sid,name,major,age,email):
        self.sid = sid
        self.name = name
        self.major = major
        self.age = age
        self.email = email

    def info(self):
        print(f'\tSID:                 {self.sid} \n' 
              f'\tStudent Name:        {self.name} \n' 
              f'\tMajor:               {self.major} \n' 
              f'\tAge:                 {self.age} \n'
              f'\tEmail:               {self.email} \n')

class Employee:
    my_employee = []
    def __str__(self,eid,name,position,age,email):
        self.eid = eid
        self.name = name
        self.position = position
        self.age = age
        self.email = email

    def info(self):
        print(f'\tEID:                  {self.eid} \n' 
              f'\tEmployee Name:        {self.name} \n'
              f'\tPosition:             {self.position} \n'
              f'\tAge:                  {self.age} \n'
              f'\tEmail:                {self.email} \n')

class Device:
    my_device = []

    def __str__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def device_info(self):
        print(f'\tBrand:                {self.brand} \n'
              f'\tModel:                {self.model} \n'
              f'\tPrice:                {self.price} \n')

class Mobile:
    my_mobile = []

    def __str__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def mobile_info(self):
        print(f'\tMobile Brand:         {self.brand} \n'
              f'\tModel:                {self.model} \n'
              f'\tPrice:                {self.price} \n')

class Tablet:
    my_tablet = []

    def __str__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def mobile_info(self):
        print(f'\tMobile Brand:         {self.brand} \n'
              f'\tModel:                {self.model} \n'
              f'\tPrice:                {self.price} \n')

class Laptop:
    my_laptop = []

    def __str__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

    def mobile_info(self):
        print(f'\tLaptop Brand:         {self.brand} \n'
              f'\tModel:                {self.model} \n'
              f'\tPrice:                {self.price} \n')