# Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

# decorator is like hiway tollbooth

# in javascript we have HOC same in python decorator have

# decorator is like e box hai usko ek pipe ke through function pass krwana

import time

def timer(func):
    # take multiple argument
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in  {end-start} ")
        return result
    
    return wrapper


# ab upar wale function ko TOLL bnana hai ki koi bhi function is se hoke hi gujre

#decorate


@timer
def example_function(n):
    time.sleep(n)


# so ab humra example_function , timer function se hoke hi gujrega because we use timer decorator(9:55:24)



example_function(2)



