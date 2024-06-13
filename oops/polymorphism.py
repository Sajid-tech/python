#  Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# Polymorphism in Python is the ability of one object to take on multiple forms.

# The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.

# in my word . polymorphism means many form , meand same function name ko diffrent types ki tarah use kr skte hai

class Car:
    def __init__(self, brand, model):
        # two time underscore in brand make it encapsulate meand private
        self.__brand = brand
        self.model = model

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

# print(my_car.get_brand())
print("mycar: ",my_car.fuel_type())

# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.__brand)
# print(my_tesla.get_brand())
print("electriccar",my_tesla.fuel_type())

# yaha pe dekha ki dono class mein method same hai but used different ho rha hai