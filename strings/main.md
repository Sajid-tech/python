# Strings in Python

PS E:\project\python\strings> python3
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep 5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> chai = "Lemon Chai"
> chai
> 'Lemon Chai'
> print(chai)
> Lemon Chai
> chai = "masala chai"
> chai  
> 'masala chai'
> first_char =chai[0]
> print(first_char)
> m
> slice_chai = cahi[0,6]
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> NameError: name 'cahi' is not defined
> slice_chai = cahi[0:6]
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> NameError: name 'cahi' is not defined
> slice_chai = chai[0:6]
> print(slice_chai)
> masala
>
> num_list ="0123456789"
> print(num_list)
> 0123456789
> num_list[3:]
> '3456789'
> num_list[:7]
> '0123456'
> num_list[0:7]
> '0123456'
> num_list[0:7:2]
> '0246'
>
> # last 2 is hoping that means
>
> num_list[0:7:3]
> '036'
> num_list[0:7:4]
> '04'
>
> chai
> 'masala chai'
> print(chai.len())
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> AttributeError: 'str' object has no attribute 'len'
> print(chai.length)
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> AttributeError: 'str' object has no attribute 'length'
> print(chai.len)  
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> AttributeError: 'str' object has no attribute 'len'
> chai
> 'masala chai'
> print(chai.upper())
> MASALA CHAI
> print(chai.lower())
> masala chai
>
> # strip() -- remove extra spaces
>
> chai = " Ginger Tea "\
> ...
> KeyboardInterrupt
> chai
> 'masala chai'
> chai = " Ginger Tea "
> chai
> ' Ginger Tea '
> print(chai.strip())
> Ginger Tea
> chai
> ' Ginger Tea '
> chai.strip()
> 'Ginger Tea'
>
> chai = "Lemon chai"
> chai
> 'Lemon chai'
> print(chai.replace("Lemon","mint"))
> mint chai
> chai
> 'Lemon chai'
>
> chai = "Ginger,Mint,Masala,Lemon"
> print(chai.split(""))
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> ValueError: empty separator
> print(chai.split())  
> ['Ginger,Mint,Masala,Lemon']
> chai  
> 'Ginger,Mint,Masala,Lemon'
> chai = "Ginger, Mint, Masala, Lemon"
> chai
> 'Ginger, Mint, Masala, Lemon'
> print(chai.split())
> ['Ginger,', 'Mint,', 'Masala,', 'Lemon']
> #print(chai.split(", "))
> #print(chai.split(", "))
> print(chai.split(", "))  
> ['Ginger', 'Mint', 'Masala', 'Lemon']
>
> chai = "Masala Chai""
> File "<stdin>", line 1

    chai = "Masala Chai""
                        ^

SyntaxError: unterminated string literal (detected at line 1)

> chai = "Masala Chai"
> print(chai.find("Chai"))
> 7
> print(chai.find("chai"))  
> -1
>
> # -1 here means if it doesnot get anything than it will return -1
>
> chai = "Masla chai chai chai "
> cahi
> Traceback (most recent call last):
> File "<stdin>", line 1, in <module>
> NameError: name 'cahi' is not defined
> chai
> 'Masla chai chai chai '
> print(chai.count("chai"))
> 3
>
> chai_type = "Masala"  
> quantity = 2
>
> # order formatting in string
>
> order = "I ordered {} cups of {} chai "
> order
> 'I ordered {} cups of {} chai '
>
> # {} --> called placeholder
>
> print(order.format(quantity,chai_type))
> I ordered 2 cups of Masala chai
>
> chai_variety = ["Lemon" , "Ginger", "Masala" ]
> chai_variety
> ['Lemon', 'Ginger', 'Masala']
>
> # To convert List into String
>
> print("".join(chai_variety)
> ...
> KeyboardInterrupt
> print("".join(chai_variety))
> LemonGingerMasala
> print(" ".join(chai_variety))
> Lemon Ginger Masala
> print("-".join(chai_variety))  
> Lemon-Ginger-Masala
> print("/".join(chai_variety))
> Lemon/Ginger/Masala
> print(", ".join(chai_variety))
> Lemon, Ginger, Masala
>
> chai
> 'Masla chai chai chai '
> chai = "Masala Chai"
> chai
> 'Masala Chai'
>
> # to find the length of the string
>
> len(chai)
> 11
>
> # letter printing
>
> for letter in chai:
> ... print(letter)
> ...
> M
> a
> s
> a
> l
> a

C
h
a
i

> chai = "He said, "Masala chai is awesome" "
> File "<stdin>", line 1

    chai = "He said, "Masala chai is awesome" "
                      ^^^^^^

SyntaxError: invalid syntax

> # to solve this err 1. is to use single quote and double quote and 2. using \
>
> chai = 'He said, "Masala chai is awesome"'  
> chai
> 'He said, "Masala chai is awesome"'
> chai = 'He said, "Masala chai is awesomes"'
> chai
> 'He said, "Masala chai is awesomes"'
> chai = "He said, \"Masala chai is good\""  
> chai
> 'He said, "Masala chai is good"'
>
> chai ="Masala\nChai"
> chai
> 'Masala\nChai'
> print(chai)
> Masala
> Chai
> chai = r"Masala\nchai"
> chai
> 'Masala\\nchai'
> print(chai)
> Masala\nchai
> chai
> 'Masala\\nchai'
> chai = r"c:\user\python\"
> File "<stdin>", line 1

    chai = r"c:\user\python\"
           ^

SyntaxError: unterminated string literal (detected at line 1)

> chai = r"c:\\user\\python\\"
> chai
> 'c:\\\\user\\\\python\\\\'
> print(chai)
> c:\\user\\python\\
> chai = r"c:\\user\\python"  
> chai
> 'c:\\\\user\\\\python'
> print(chai)
> c:\\user\\python
> chai = r"c:\user\python"  
> chai
> 'c:\\user\\python'
> print(chai)
> c:\user\python
> chai = "c:\user\python"  
>  File "<stdin>", line 1

    chai = "c:\user\python"
                           ^

SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape

> chai = "c:\\user\\python"
> chai
> 'c:\\user\\python'
> print(chai)
> c:\user\python

> chai = "Masala Chai"  
> print("Masala" in chai)  
> True
> print("Masssala" in chai)
> False
