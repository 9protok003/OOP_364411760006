from EvCar import thaievcar

def display_option():
    print("\n")
    print("[ Welcome to Vehicle EvCar Data Store System ]")
    print("\n-------------------------------")
    print("| 1. Add Vehicle                |")
    print("| 2. Display all vehicle        |")
    print("| 3. Delete Vehicle             |")
    print("| 4. Edit Vehicle Price         |")
    print("| 5. Exit                       |")
    print("-------------------------------\n")
    select = int(input("Select (1-5)? : "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        delete_vehicle()
    elif select == 4:
        edit_vehicle_price()
    elif select == 5:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, Select Number 1-5")

def input_vehicle_data():
    brand = input("Enter vehicle brand: ")
    model = input("Enter vehicle model: ")
    acceleration_rate = float(input("Enter vehicle acceleration_rate: "))
    hp = input("Enter vehicle hp: ")
    maxspeed = input("Enter vehicle maxspeed: ")
    price = input("Enter vehicle price: ")

    thaievcar.my_thaievcar.append(thaievcar(brand,model,acceleration_rate,hp,maxspeed,price))
    print("\n-------------------------------")
    print("Already add vehicle to store.")
    print("-------------------------------\n")

def display_vehicle():
    if len(thaievcar.my_thaievcar) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(thaievcar.my_thaievcar)} following.')
        n = 1
        for x in thaievcar.my_thaievcar:
            print(f'Car_ID: [{n}]' ,end=" ")
            x.thaievcar_detail()
            n = n+1
        print("\n")

def delete_vehicle():
    display_vehicle()
    if len(thaievcar.my_thaievcar) != 0:
        s = int(input("Select to delete? : "))

        thaievcar.delete_vehicle(thaievcar, s-1)
        print("\n-------------------------------")
        print("Your data has been deleted.")
        print("-------------------------------\n")

def edit_vehicle_price():
    display_vehicle()
    if len(thaievcar.my_thaievcar) != 0:
        s = int(input("Select to edit? : "))

        print(f'Previous price : {thaievcar.my_thaievcar[s-1].price}')
        new_price = float(input("New price : "))
        thaievcar.edit_vehicle_price(thaievcar,s-1,new_price)

s = 0
while s == 0:
    display_option()
