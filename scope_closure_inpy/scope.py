username = "chaicode"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99 #global value

def func2(y):
    z = x+y
    return z

result = func2(1)

print(result)


# def func3():
#     global x  # if you do this and than this x will be become global but do not do this , avoid this 
#     x = 12
   
# func3()
# print(x)


# closure 

def f1():
    x = 88
    def f2():
        print(x)
    return f2
myresult = f1()

myresult()


# eg

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual # here only defnitation return 

result_chai = chaicoder(3)

print(result_chai(5))
