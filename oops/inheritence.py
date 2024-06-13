# 3. Inheritance
# Problem: Create an Electric Car class that inherits from the Car class and has an additional attribute battery_size.

# inheritence is like that inherit from parents

#Inheritance is the capability of one class to inherit the properties from another class.

# It specifies that the child object acquires all the properties and behaviors of the parent object.

# super() means ye kaam super mein ho chuka hai matlab apne se upar class mein 

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

# inherit from car -- just add class name
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        # super: to get parameter of car class
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("tesla","Model S", "85kwh")    
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.battery_size)

# my_car = Car("Toyota","Corala")


# print(my_car.full_name())