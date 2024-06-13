# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.


# to check use isInstance(objectvaribale,classname)

class Car:

    def __init__(self, brand, model):
        # two time underscore in brand make it encapsulate meand private
        self.__brand = brand
        # 
        self.__model = model

      
    # make private: brand attribute : getter method 

    def get_brand(self):
        return self.__brand + " !"


    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def fuel_type(self):
        return "Petrol and disel"
    
    # static method: 
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    # for model make readonly
    @property
    def model(self):
        return self.__model
    
# inherit

class ElectricCar(Car):
    
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"

my_tesla = ElectricCar("tesla", "model S", "85kwh")

# to check mytesla is an instance of car and electric instance

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))


my_car = Car("Toyota","Corola")







