# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# It describes the idea of wrapping data and the methods that work on data within one unit.

# in simple word encapsulation is like "capsoule" jisme andar methods and data wrap hai in one unit , now you get the idea

# is  question mein car ke brand attributes of encapsulate krna hai meand private krna hai , jb mein chau pta chle

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
    
# inherit

class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("tesla", "model S", "85kwh")

my_car = Car("Toyota","Corola")

print(my_car.get_brand())

# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.__brand)
print(my_tesla.get_brand())

