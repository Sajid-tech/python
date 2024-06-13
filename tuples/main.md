# tuples

PS E:\project\python\tuples> python3
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep 5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > tea_types = ("Black", "Green", "Oolong")
> > > tea_types
> > > ('Black', 'Green', 'Oolong')
> > > tea_types[1]
> > > 'Green'
> > > tea_types[-1]
> > > 'Oolong'
> > > tea_types[1:]
> > > ('Green', 'Oolong')
> > >
> > > tea_types[0] = "Lemon"
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: 'tuple' object does not support item assignment
> > >
> > > len(tea_types)
> > > 3
> > >
> > > more_tea = ("Herbal", "Earl Grey")
> > > all_tea = more_tea + tea_types
> > > all_tea
> > > ('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolong')
> > >
> > > if "Green" in all_tea:
> > > ... print("I have Green tea")
> > > ...
> > > I have Green tea
> > >
> > > more_tea = ("Herbal", "Earl Grey", "Herbal")
> > > more_tea
> > > ('Herbal', 'Earl Grey', 'Herbal')
> > > more_tea.count("Herbal")
> > > 2
> > > more_tea.count("Herbl")  
> > > 0
> > > more_tea.count("Earl grey")
> > > 0
> > > more_tea.count("Earl Grey")
> > > 1
> > >
> > > tea_types
> > > ('Black', 'Green', 'Oolong')
> > > (black, green, Oolong) = tea_types
> > > tea_types
> > > ('Black', 'Green', 'Oolong')
> > > black
> > > 'Black'
> > > green
> > > 'Green'
> > >
> > > type(tea_types)
> > > <class 'tuple'>
