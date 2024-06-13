# banana_color = input("whats your banana color: ")

# if (banana_color == 'Green'):
#     print("Banana is Unripe")
# elif (banana_color == 'Yellow'):
#     print("Banana is Ripe")
# elif (banana_color == 'Brown'):
#     print("Banana is Overripe")


fruit = input("Whats your Fruit name: ")

if fruit != "Banana":
    print("I don't have information about it: ")
    exit()

color = input("Whats your banana color: ")



if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")



