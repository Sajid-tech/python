distance = float(input("Tell me your distance(km): "))

if (distance < 3):
    mode = "Walk"
elif (distance <15):
    mode ="Bike"
else:
    mode =" Car"

print("mode:",mode)