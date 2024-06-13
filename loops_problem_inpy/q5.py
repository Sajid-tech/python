input_str = "eeterch"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break


# continue ke andar sirf ek iteration khatam hota hai 
# but break ke andar pura loop khatam ho jata hai

