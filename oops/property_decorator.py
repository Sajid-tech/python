# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

# decorator : one decorator (@staticmethod) we already used now we will know about property decorator


# first method to make model readonly
# 1. make model private
#2. ek method bnana hoga same attribute name se

    # def model(self):
        # return self.__model

#3. use phle ek property decorater use krna hoga
'''
 @property
    def model(self):
        return self.__model
'''
# important note 

# property decorator use kr rhe hai toh means  aap us attribute ko future meinkabhi change nhi krna chah rhe hai sirf vo readonly hoga, aur use read method se krenge but call as attribute hi hoga not model






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

my_car = Car("Toyota","Corola")
# my_car.model = "city" # here we can overrite the model but we have to make it readonly

print(my_car.model)






