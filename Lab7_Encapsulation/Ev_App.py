from Ev import Thaievcar

# e = Thaievcar(1001,"Tesla","Model 3",6.1,347,559,1759000)

# display data by using gatter
# print(e.get_car_id(),e.get_brand(),e.get_model())

# e.Thaievcar_detail()

# e.set_price(1500000)
# e.Thaievcar_detail()

def display_option():
    print("\n")
    print("[ Welcome to Vehicle EvCar Data Store System ]")
    print("\n---------------------------------")
    print("| 1. เพิ่มข้อมูลรถ                   |")
    print("| 2. แสดงข้อมูลรถทั้งหมด             |")
    print("| 3. ออก                        |")
    print("---------------------------------\n")
    select = int(input("Select (1-3)? : "))
    if select == 1:
        input_vehicle_data()
    elif select == 2:
        display_vehicle()
    elif select == 3:
        print("Good Bye.")
        exit(0)
    else:
        print("Pleaes, Select Number 1-3")

def input_vehicle_data():
    brand = input("ยี่ห้อ : ")
    model = input("รุ่น : ")
    acceleration_rate = float(input("อัตราเร่ง : "))
    hp = input("แรงม้า : ")
    maxspeed = input("ความเร็ว : ")
    price = input("ราคา : ")

    Thaievcar.my_Thaievcar.append(Thaievcar(brand,model,acceleration_rate,hp,maxspeed,price))
    print("\n-------------------------------")
    print("      บันทักข้อมูลรถเรียบร้อยแล้ว.")
    print("-------------------------------\n")

def display_vehicle():
    if len(Thaievcar.my_Thaievcar) ==0:
        print("ไม่มีรถอยู่ใน")
    else:
        print(f'You had {len(Thaievcar.my_Thaievcar)} following.')
        n = 1
        for x in Thaievcar.my_Thaievcar:
            print(f'Car_ID: [{n}]' ,end=" ")
            x.Thaievcar_detail()
            n = n+1
        print("\n")

s = 0
while s == 0:
    display_option()