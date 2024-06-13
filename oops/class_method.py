# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# class ke andar self ek telephone ki tarah kaam krta hai vo jo method niche call hogi uska aur method ke beech always use self


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car("Toyota","Corala")

print(my_car.brand)
print(my_car.full_name())
