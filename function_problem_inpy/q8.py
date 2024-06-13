# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

# question says like this
'''
def print_kwargs(name,power):
        print("Name",name ," Power ", power)


print_kwargs(name= "sajid",power= "coding") 
print_kwargs(name= "sajid") 
print_kwargs(name= "sajid",power= "coding" , anime="Naruto") 

'''

# to handle key and value in arguments


def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name= "sajid",power= "coding") 
print_kwargs(name= "sajid") 
print_kwargs(name= "sajid",power= "coding" , anime="Naruto")
