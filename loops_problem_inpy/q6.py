# Problem: Compute the factorial of a number using a while loop.


number = 5

factorial = 1

while number > 0:
    print("start factorial: ",factorial)
    print("start number : ",number)
    factorial = factorial * number
    print("after factorial before -1: ",factorial)
    print("before redice -1: ",number)
    number -= 1
    print("after reduce -1: ",number)
print(factorial) 