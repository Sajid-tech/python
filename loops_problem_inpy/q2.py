input = int(input("Tell me you number under 100: "))

sum_even = 0

for i in range(1,input+1):
    if i%2 == 0:
        sum_even +=1
print("Even count of number is : ", sum_even)


