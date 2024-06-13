PS E:\project\python\function_problem_inpy> python3
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep 5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > f = open('bts_inloop.py')
> > >
> > > # to read the file
> > >
> > > f.readline()
> > > 'import time \n'
> > > f.readline()
> > > 'print("chai is here")\n'
> > > f.readline()
> > > 'username = "sajid"\n'
> > > f.readline()
> > > 'print(username)\n'
> > > f.readline()
> > > ''
> > > f.readline()
> > > ''
> > > f.readline()
> > > ''
> > > f.readline()
> > > ''
> > > f = open('bts_inloop.py')
> > >
> > > # wapis se file load ho gyi hai
> > >
> > > f.**next**()
> > > 'import time \n'
> > > f.**next**()
> > > 'print("chai is here")\n'
> > > f.**next**()
> > > 'username = "sajid"\n'
> > > f.**next**()
> > > 'print(username)\n'
> > > f.**next**()
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > StopIteration
> > >
> > > # to read file as a loop because file is iterable
> > >
> > > for line in open('bts_inloop.py'):
> > > ... print(line)
> > > ...
> > > import time

print("chai is here")

username = "sajid"

print(username)

> > > for line in open('bts_inloop.py'):
> > > ... print(line, end = '')
> > > ...
> > > import time
> > > print("chai is here")
> > > username = "sajid"
> > > print(username)
> > >
> > > # by while loop
> > >
> > > f = open('bts_inloop.py')  
> > > while True:
> > > ... line = f.readline()
> > > ... if not line: break
> > > ... print(line, end='')
> > > ...
> > > import time
> > > print("chai is here")
> > > username = "sajid"
> > > print(username)
> > >
> > > test = "sajid"
> > > if not test:
> > > ... print("chai")
> > > ...
> > > test = ""  
> > > if not test:  
> > > ... print("chai")
> > > ...
> > > chai
> > >
> > > myList = [1,2,3,4]
> > > I = iter(myList)
> > > I
> > > <list_iterator object at 0x0000021346E7AF80>
> > >
> > > # humne jo list bnani n vo us point object pe refernce kr rha hai , memor
> > >
> > > y ka starting point
> > > I.**next**()  
> > > 1
> > > I.**next**()
> > > 2
> > > I.**next**()
> > > 3
> > > I.**next**()
> > > 4
> > > I.**next**()
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > StopIteration
> > >
> > > f = open('bts_inloop.py')
> > > iter(f) is f
> > > True
> > > iter(f) is f.**iter**()
> > > True
> > >
> > > # its is same for file not for list
> > >
> > > myNewList = [1,2,3]
> > > iter(myNewList) is myNewList
> > > False
> > >
> > > # jab file ko aap stored lete ho ek refernce mein toh voh ek already iterable object hai but list ka agar apne kisi memory refernce mein naam diya hai vo uska iterable object nhi hai

> > > # Dictornary is also iterterable
> > >
> > > D = {'a':1,'b':2}
> > > for key in D.keys():
> > > ... print(key)
> > > ...
> > > a
> > > b
> > > I = iter(D)
> > > I
> > > <dict_keyiterator object at 0x0000021346EA5170>
> > > next(I)
> > > 'a'
> > >
> > > next(I)
> > > 'b'
> > > next(I)
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > StopIteration
> > >
> > > # range is also iterrable
> > >
> > > range(5)
> > > range(0, 5)
> > > R =range(5)
> > > R
> > > range(0, 5)
> > > I = iter(R)
> > > next(I)
> > > 0
> > > next(I)
> > > 1
> > > next(I)
> > > 2
> > > next(I)
> > > 3
> > > next(I)
> > > 4
> > > next(I)
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > StopIteration
