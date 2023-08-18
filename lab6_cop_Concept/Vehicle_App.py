from oppvehiclech6 import Vehicle

# option
def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Display all vehicle")
    print("3.exit")
    select = int(input("select (1-3)?: "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, select number 1-3")

# Add Data
def input_vehicle_data(my=None):
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    color = input("Enter vehicle color: ")
    maxspeed = input("Enter vehicle maxspeed: ")
    price = float(input("Enter vehicle price: "))


    my.vehicle.append(Vehicle(brand,model,color,maxspeed.price))
    print("\n-------------------------------")
    print("Already add vehicle to store.")
    print("\n-------------------------------")

# Display data
def display_vehicle():
    if len(my.vehicle) ==0:
        print("Yot had no vehicle data.")
    else:
        print(f'You had {len(my_vehicle)} following.')
        for x in my_vehicle:
            x.vehicle.info()
        print("\n")

my_vehicle = []
s = 0
while s == 0:
    display_option()