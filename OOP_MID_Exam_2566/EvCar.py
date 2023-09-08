
class thaievcar:
    my_thaievcar = []

    def __init__(self,model,brand,acceleration_rate,hp,maxspeed,price):
        self.model = model
        self.brand = brand
        self.acceleration_rate = acceleration_rate
        self.hp = hp
        self.maxspeed = maxspeed
        self.price = price

    def thaievcar_detail(self):
        print(f'Model : {self.model} '
              f'Brand : {self.brand} '
              f'Acceleration_Rate : {self.acceleration_rate} '
              f'HP :{self.hp} '
              f'MaxSpeed : {self.maxspeed} '
              f'Price : {self.price} ')

    def delete_vehicle(self,index):
        self.my_thaievcar.pop(index)

    def edit_vehicle_price(self,index,new_price):
        self.my_thaievcar.pop(index).price = new_price