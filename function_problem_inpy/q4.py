#  Create a function that returns both the area and circumference of a circle given its radius.

import math

def area(r):
    return 3.14 * r **2
print(area(5))

def circum(r):
    return 2 * 3.14 * r
print(circum(2))

# using import math

def area_area(radius):
    area = math.pi * radius ** 2
    circumference = 2* math.pi * radius

    return area,circumference

a,c = area_area(2)
print("Area: ",math.floor(a), "Circum: ", c)

# retrun jha lga doge mtlb vo execute ho jayega aur vahi exit ho jayega aur niche kuch nhi print krega