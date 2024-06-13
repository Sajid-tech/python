# prime number checker

# number divide by 1 or itself

number = int(input("Enter the number to check no is prime or not: "))

is_prime = True

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            is_prime = False
            break

print("number is a prime number: ", is_prime)

