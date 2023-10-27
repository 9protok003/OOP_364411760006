
class Person:
    def __str__(self,pname,page,pemail):
        self.pname = pname
        self.page = page
        self.pemail = pemail

    def info(self):
        print(f'\tPerson Name:         {self.pname} \n' 
              f'\tAge:                 {self.page} \n' 
              f'\tEmail:               {self.pemail} \n')

class Student:
    def __str__(self,sid,sname,smajor,sage,semail):
        self.sid = sid
        self.sname = sname
        self.smajor = smajor
        self.sage = sage
        self.semail = semail

    def info(self):
        print(f'\tSID:                 {self.sid} \n' 
              f'\tStudent Name:        {self.sname} \n' 
              f'\tMajor:               {self.smajor} \n' 
              f'\tAge:                 {self.sage} \n'
              f'\tEmail:               {self.semail} \n')

class Employee:
    def __str__(self,eid,ename,eposition,eage,eemail):
        self.eid = eid
        self.ename = ename
        self.eposition = eposition
        self.eage = eage
        self.eemail = eemail

    def info(self):
        print(f'\tEID:                  {self.eid} \n' 
              f'\tEmployee Name:        {self.ename} \n'
              f'\tPosition:             {self.eposition} \n'
              f'\tAge:                  {self.eage} \n'
              f'\tEmail:                {self.eemail} \n')

class Device:
    my_device = []

    def __str__(self,dbrand,dmodel,dprice):
        self.dbrand = dbrand
        self.dmodel = dmodel
        self.dprice = dprice

    def device_info(self):
        print(f'\tBrand:                {self.dbrand} \n'
              f'\tModel:                {self.dmodel} \n'
              f'\tPrice:                {self.dprice} \n')

class Mobile:
    my_mobile = []

    def __str__(self,mbrand,mmodel,mprice):
        self.mbrand = mbrand
        self.mmodel = mmodel
        self.mprice = mprice

    def mobile_info(self):
        print(f'\tMobile Brand:         {self.mbrand} \n'
              f'\tModel:                {self.mmodel} \n'
              f'\tPrice:                {self.mprice} \n')

class Tablet:
    my_tablet = []

    def __str__(self,tbrand,tmodel,tprice):
        self.tbrand = tbrand
        self.tmodel = tmodel
        self.tprice = tprice

    def mobile_info(self):
        print(f'\tMobile Brand:         {self.tbrand} \n'
              f'\tModel:                {self.tmodel} \n'
              f'\tPrice:                {self.tprice} \n')

class Laptop:
    my_laptop = []

    def __str__(self,lbrand,lmodel,lprice):
        self.lbrand = lbrand
        self.lmodel = lmodel
        self.lprice = lprice

    def mobile_info(self):
        print(f'\tLaptop Brand:         {self.lbrand} \n'
              f'\tModel:                {self.lmodel} \n'
              f'\tPrice:                {self.lprice} \n')




























class Vaccine:
    all_vaccine = ["sinovac" , "astrazeneca" , "johnson&johnson" ,
                   "moderna" , "sinopharm" , "pfizer"]
    def __init__(self,vacc_name):
        self.__vacc_name = vacc_name

        # getter and setter
    def get_vacc_name(self):
        return self.__vacc_name
    def set_vacc_name(self,new_vacc_name):
        self.__vacc_name = new_vacc_name
    def info(self):
        print(f'Vaccine:                {self.__vacc_name} \n')

class Vaccine_Passport:
    def __init__(self,Student):
        self.student = Student
        self.vaccinated = list()
        self.date = list()

    def add_vaccinated(self,vac):
        self.vaccinated.append(vac)

    def add_date(self,date):
        self.date.append(date)

    def info(self):
        # 1.display student info
        print("Student information: ")
        self.student.info()
        # 2.display vaccine info
        print(f'\tVaccinated of {self.student.name}: ')
        if len(self.vaccinated) == 0:
            print(f'\tNo vaccinated data.')
        else:
            #n = 0
            for x in range(len(self.vaccinated)):
                print(f'\tvaccine {x+1}. {self.vaccinated[x].get_vacc_name()} \tdate: {self.date[x]}')


