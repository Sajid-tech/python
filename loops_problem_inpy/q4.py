input_str = input("Revrese the string: ")

reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str
print(reversed_str)