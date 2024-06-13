# Create a Car class with attributes like brand and model. Then create an instance of this class.

# class
# convention of class - first letter capital

# in javscript this = self

# class is like blurprint , ek form ki tarah jise koi bhi blueprint ki tarah use kr skta hai

# jab class of varivale mein stored krte hai toh vo object hoat hai

# same class ka do variable bnayege toh dono ka object alag hoga

# self.brand ka matlab hai class ke andar ka variable

# jb class ke andar ka access lena hai toh "self " likhna padega n

# __init_ is nothing but like constructor



class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Toyota","Corola") # here my_car is object

print(my_car.brand)
print(my_car.model)

my_new_car = Car("Tata","Safari")

print(my_new_car.model)