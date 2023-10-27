from models import Person, Student, Employee, Tablet, Laptop, Mobile

def display_option():
    print("User Data")
    print("\n-------------------------------")
    print("1.Add user")
    print("2.Add device for")
    print("3.Display devices information")
    print("4.exit")
    print("-------------------------------\n")
    select = int(input("select (1-4)?: "))
    if select == 1:
        input_user_data()
    # elif select == 2:
    #     display_vehicle()
    # elif select == 3:
    #     delete_vehicle()
    elif select == 4:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, select number 1-5")


def input_user_data():
    pname = input("Enter vehicle brand: ")
    page = input("Enter vehicle model: ")
    pemail = input("Enter vehicle color: ")

    vehicle.my_vehicle.append(vehicle(brand,model,color,maxspeed,price))
    print("\n-------------------------------")
    print("Already add vehicle to store.")
    print("-------------------------------\n")



s = 0
while s == 0:
    display_option()