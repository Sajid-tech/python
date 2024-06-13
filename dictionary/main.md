# Dictionary in Python

PS E:\project\python\dictionary> python3
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep 5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > # to create dict
> > >
> > > chai_type ={"Masala":"Spicy", "Ginger": "Zesty", "Green" : "mild"}
> > > chai_type
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'mild'}
> > > chai_type[0]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > KeyError: 0
> > > chai_type["Green"]
> > > 'mild'
> > > chai_type.get("Ginger")
> > > 'Zesty'
> > >
> > > chai_type  
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'mild'}
> > > chai_type["Green"] = "Fresh"
> > > chai_type
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
> > >
> > > for chai in chai_type:
> > > ... print(chai)
> > > ...
> > > Masala
> > > Ginger
> > > Green
> > >
> > > for chai in chai_type:
> > > ... print(chai, chai_type[chai])
> > > ...
> > > Masala Spicy
> > > Ginger Zesty
> > > Green Fresh
> > >
> > > for key, values in chai_type.items():
> > > ...  
> > >  File "<stdin>", line 2

    ^

IndentationError: expected an indented block after 'for' statement on line 1

> > > for key, value in chai_type.items():  
> > > ... print(key, value)
> > > ...
> > > Masala Spicy
> > > Ginger Zesty
> > > Green Fresh
> > >
> > > if "Masala" in chai_type:
> > > ... print("I have masala chai")
> > > ...
> > > I have masala chai
> > >
> > > print(len(chai_type))
> > > 3
> > >
> > > chai_type
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
> > >
> > > chai_type["Earl Grey"] = "Citrus"
> > > chai_type
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
> > >
> > > # pop methos
> > >
> > > chai_type.pop("Ginger")
> > > 'Zesty'
> > > chai_type  
> > > {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
> > >
> > > chai_type.popitem()  
> > > ('Earl Grey', 'Citrus')
> > > chai_type
> > > {'Masala': 'Spicy', 'Green': 'Fresh'}
> > >
> > > # delete from memory
> > >
> > > del chai_type["Green"]
> > > chai_type
> > > {'Masala': 'Spicy'}
> > > chai_type_copy = chai_type.copy()
> > >
> > > tea_shop ={  
> > > ... "chai" : {"Masala": "Spicy","Ginger":"Zesty"},
> > > ... "Tea" :{"Green":"Mild" ,"Black":"Strong"}
> > > ... }
> > > tea_shop
> > > {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
> > > print(tea_shop)
> > > {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
> > > tea.shop.get("chai")
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'tea' is not defined
> > > tea_shop.get("chai")
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty'}
> > > tea_shop.get("chai").get("Masala")
> > > 'Spicy'
> > >
> > > # or
> > >
> > > tea_shop["chai"]
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty'}
> > > tea_shop["chai"]["Ginger"]
> > > 'Zesty'
> > >
> > > tea_shop.get("chai","Ginger")  
> > > {'Masala': 'Spicy', 'Ginger': 'Zesty'}
> > >
> > > squared_num = {x:x\*\*2 for x in range(7)}  
> > > squared_num
> > > {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
> > >
> > > # keys ka set
> > >
> > > keys = ["Masala","Ginger","Lemon"]
> > > keys
> > > ['Masala', 'Ginger', 'Lemon']
> > > default_value = "Delecious"
> > > new_dict = dict.fromkeys(keys,default_value)
> > > new_dict
> > > {'Masala': 'Delecious', 'Ginger': 'Delecious', 'Lemon': 'Delecious'}
> > > new_dict = dict.fromkeys(keys,keys)  
> > > new dict
> > > File "<stdin>", line 1

    new dict
        ^^^^

SyntaxError: invalid syntax

> > > new_dict
> > > {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
