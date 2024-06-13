# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

#instance means object

# static methods means use class ke methods ko 
# class. krke bhi access kr skte hai vo class se bound hota hai 

# a static method is bound to a class rather than the objects for that class


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
    
    # static method: 
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
# inherit

class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("tesla", "model S", "85kwh")

my_car = Car("Toyota","Corola")

# print("mycar: ",my_car.general_description())
print(Car.general_description())


# class_varibale question no 6
print(Car.total_car)


