order_size = input("Tell me whats you like coffee, medium, small or large: ")

extra_shot = input("Do you want extra shot (Yes or No) : ").strip().lower()

if (extra_shot == "yes"):
    coffee = order_size + "Coffee with extra shot"
else:
    coffee = order_size + "coffee"

print("Order:", coffee)