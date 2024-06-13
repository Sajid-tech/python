# input
# while loop


# input =[1,2,3,4,5,6,7,8,9,10]

while True:
    number = int(input("Enter Value between 1 and 10: "))
    if number in range(1,11):
        print("Thanks")
        break
    else:
        print("Invalid number , Try again")

