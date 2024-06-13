password = input("tell me your password: ")
password_strength = len(password)

if password_strength < 6:
    print("Weak")
elif password_strength < 10:
    print("Medium")
else:
    print("Strong")