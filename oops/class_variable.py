# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car:
    total_car = 0

    def __init__(self, brand, model):
        # two time underscore in brand make it encapsulate meand private
        self.__brand = brand
        self.model = model

        # to track numbe of car created
        Car.total_car += 1

    # make private: brand attribute : getter method 

    def get_brand(self):
        return self.__brand + " !"


    def full_name(self):
        return f"{self.__brand} {self.model}"
    def fuel_type(self):
        return "Petrol and disel"
    
# inherit

class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("tesla", "model S", "85kwh")

my_car = Car("Toyota","Corola")
# my_car_two = Car("Tata","nexon")

# print(my_car.get_brand())
print("mycar: ",my_car.get_brand())


# car tracking
print(Car.total_car)



# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
print("electriccar",my_tesla.fuel_type())
