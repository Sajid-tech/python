# List in Python

PS E:\project\python\list-python> python3
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep 5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > import os
> > > os.getcwd()
> > > 'E:\\project\\python\\list-python'
> > > tea*varities = ["Black", "Green", "Oolong", "White"]
> > > tea_varities
> > > ['Black', 'Green', 'Oolong', 'White']
> > > print(tea_varities)*
> > > File "<stdin>", line 1

    print(tea_varities)_
                       ^

SyntaxError: invalid syntax

> > > print(tea_varities)
> > > ['Black', 'Green', 'Oolong', 'White']
> > >
> > > # to get indivisul item
> > >
> > > print(tea_varities[1])  
> > > Green
> > > print(tea_varities[-1])
> > > White
> > > print(tea_varities[1:3])
> > > ['Green', 'Oolong']
> > > print(tea_varities[:3])  
> > > ['Black', 'Green', 'Oolong']
> > > tea_varities[3]
> > > 'White'
> > > tea_varities[3] = "Herbal"
> > > print(tea_varities)  
> > > ['Black', 'Green', 'Oolong', 'Herbal']
> > >
> > > #treat as an array  
> > > tea_varities[1:3] = "Lemon"
> > > print(tea_varities)
> > > ['Black', 'L', 'e', 'm', 'o', 'n', 'Herbal']
> > > tea_varities[1] = "Green"  
> > > print(tea_varities)  
> > > ['Black', 'Green', 'e', 'm', 'o', 'n', 'Herbal']
> > > tea_varities = ["Black", "Green", "Oolong", "White"]
> > > print(tea_varities)  
> > > ['Black', 'Green', 'Oolong', 'White']
> > > tea_varitie[1:3] = ["Sajid"]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'tea_varitie' is not defined. Did you mean: 'tea_varities'?
> > > tea_varities[1:2] = ["Sajid"]
> > > print(tea_varities)  
> > > ['Black', 'Sajid', 'Oolong', 'White']
> > >
> > > tea_varities[1:3]  
> > > ['Sajid', 'Oolong']
> > > tea_varities[1:3] = ["Majid", "Wajid"]
> > > tea_varities[1:3]  
> > > ['Majid', 'Wajid']
> > > tea_varities  
> > > ['Black', 'Majid', 'Wajid', 'White']
> > >
> > > tea_varities
> > > ['Black', 'Majid', 'Wajid', 'White']
> > >
> > > # loop
> > >
> > > for tea in tea_varities
> > > File "<stdin>", line 1

    for tea in tea_varities
                           ^

SyntaxError: expected ':'

> > > for tea in tea_varities:
> > > ... print(tea)
> > > ...
> > > Black
> > > Majid
> > > Wajid
> > > White
> > >
> > > for tea in tea_varities:
> > > ... print(tea, end="-")
> > > ...  
> > > Black-Majid-Wajid-White->>>
> > >
> > > if "Oolong" in tea_varities:
> > > ... print("I have Oolong tea")
> > > ...
> > > tea_varities.append("Oolong")
> > > tea_varities
> > > ['Black', 'Majid', 'Wajid', 'White', 'Oolong']
> > > if "Oolong" in tea_varities:  
> > > ... print("I have Oolong tea")
> > > ...
> > > I have Oolong tea
> > >
> > > tea_varities  
> > > ['Black', 'Majid', 'Wajid', 'White', 'Oolong']
> > > tea_varities.pop()
> > > 'Oolong'
> > > tea_varities  
> > > ['Black', 'Majid', 'Wajid', 'White']
> > >
> > > # pop() will eject last value of list
> > >
> > > tea_varities.remove("Majid")
> > > tea_varities
> > > ['Black', 'Wajid', 'White']
> > >
> > > # insert method
> > >
> > > tea_varities.insert(1,"green")
> > > tea_varities  
> > > ['Black', 'green', 'Wajid', 'White']
> > >
> > > tea_varities_copy = tea_varities
> > > tea_varities
> > > ['Black', 'green', 'Wajid', 'White']
> > > tea_varities_copy  
> > > ['Black', 'green', 'Wajid', 'White']
> > > tea_varities_copy = tea_varities.copy()
> > > tea_varities_copy
> > > ['Black', 'green', 'Wajid', 'White']
> > >
> > > # copy of memory refercne tea_varities_copy = tea_varities.copy()
> > >
> > > tea_varities_copy
> > > ['Black', 'green', 'Wajid', 'White']
> > > tea_varities_copy.append("Lemon")
> > > tea_varities_copy
> > > ['Black', 'green', 'Wajid', 'White', 'Lemon']
> > > tea_varities  
> > > ['Black', 'green', 'Wajid', 'White']
> > >
> > > tea_varities
> > > ['Black', 'green', 'Wajid', 'White']
> > > tea_varities_copy
> > > ['Black', 'green', 'Wajid', 'White', 'Lemon']
> > > tea_varities_copy
> > > ['Black', 'green', 'Wajid', 'White', 'Lemon']
> > >
> > > # list comprehension
> > >
> > > range(10)  
> > > range(0, 10)
> > > print(range(10))
> > > range(0, 10)
> > > y = range(10)  
> > > y
> > > range(0, 10)
> > >
> > > squared_num = [x**2 for x in range(10)]
> > > squared_num
> > > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
> > >
> > > cube_num = [x**3 for x in range(10)]
> > > cube_num
> > > [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
> > > squared_num
> > > [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
