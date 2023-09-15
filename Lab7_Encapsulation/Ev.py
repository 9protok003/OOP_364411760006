
class Thaievcar:
    my_Thaievcar = []

    def __init__(self,model,brand,acceleration_rate,hp,maxspeed,price):
        self.__model = model
        self.__brand = brand
        self.__acceleration_rate = acceleration_rate
        self.__hp = hp
        self.__maxspeed = maxspeed
        self.__price = price

    def Thaievcar_detail(self):
        print(f'Model : {self.__model} '
              f'Brand : {self.__brand} '
              f'Acceleration_Rate : {self.__acceleration_rate} '
              f'HP :{self.__hp} '
              f'MaxSpeed : {self.__maxspeed} '
              f'Price : {self.__price} ')

# getter and setter

    def get_car_id(self):  # Car_ID
        return self.__carid
    def set_car_id(self,new_carid):
        self.__carid = new_carid

    def get_model(self):  # Model
        return self.__model
    def set_salary(self,new_model):
        self.__model = new_model

    def get_brand(self):  # Brand
        return self.__brand
    def set_brand(self,new_brand):
        self.__brand = new_brand

    def get_acceleration_rate(self):  # Acceleration_Rate
        return self.__acceleration_rate
    def set_acceleration_rate(self,new_acceleration_rate):
        self.__acceleration_rate = new_acceleration_rate

    def get_hp(self):  # Hp
        return self.__hp
    def set_hp(self,new_hp):
        self.__hp = new_hp

    def get_maxspeed(self):  # Max Speed
        return self.__maxspeed
    def set_maxspeed(self,new_maxspeed):
        self.__acceleration_rate = new_maxspeed

    def get_price(self):  # Price
        return self.__price
    def set_price(self,new_price):
        self.__price = new_price

