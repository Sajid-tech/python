# Problem: Write a function that takes variable number of arguments and returns their sum.

# question says function mein kitne bhi multiple argument parameter de vo print kre 
#  eg niche hai 
# def sum_all():
#     pass

# print(sum(1,2))
# print(sum(1,2,6))
# print(sum(1,2,6,9,8))

# output

def sum_all(*args):
    for i in args:
        print(i**2)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,6,8))
print(sum_all(1,2,6,8,964,5))

