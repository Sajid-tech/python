# Numbers in Python

- in python number precison is almost infinity

PS E:\project\python\numbers> python3
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep 5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

> > > x = 2
> > > y = 3
> > > z =4
> > > x + y
> > > 5
> > > z-y
> > > 1
> > > y **4
> > > 81
> > > (x+y)**2
> > > 25
> > > (x+y)*z
> > > 20
> > > x +y *z
> > > 14
> > > 40+2.23
> > > 42.23
> > > 'sajid' + 3
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: can only concatenate str (not "int") to str
> > > int(2.23) + 40
> > > 42
> > > float(40) + 20.26
> > > 60.260000000000005
> > > 'chai' + 'code'
> > > File "<stdin>", line 1

    'chai' + 'code'

IndentationError: unexpected indent

> > > 'chai' + 'code'
> > > 'chaicode'
> > > 'chai' + ' code'
> > > 'chai code'
> > >
> > > x,y,z
> > > (2, 3, 4)
> > > x +1 ,y *2 ,z -1
> > > (3, 6, 3)
> > > y % 2
> > > 1
> > > z \*\* 2
> > > 16
> > > 2*10000
> > > 20000
> > > 2\*\*10000
> > > 19950631168807583848837421626835850838234968318861924548520089498529438830221946631919961684036194597899331129423209124271556491349413781117593785932096323957855730046793794526765246551266059895520550086918193311542508608460618104685509074866089624888090489894838009253941633257850621568309473902556912388065225096643874441046759871626985453222868538161694315775629640762836880760732228535091641476183956381458969463899410840960536267821064621427333394036525565649530603142680234969400335934316651459297773279665775606172582031407994198179607378245683762280037302885487251900834464581454650557929601414833921615734588139257095379769119277800826957735674444123062018757836325502728323789270710373802866393031428133241401624195671690574061419654342324638801248856147305207431992259611796250130992860241708340807605932320161268492288496255841312844061536738951487114256315111089745514203313820202931640957596464756010405845841566072044962867016515061920631004186422275908670900574606417856951911456055068251250406007519842261898059237118054444788072906395242548339221982707404473162376760846613033778706039803413197133493654622700563169937455508241780972810983291314403571877524768509857276937926433221599399876886660808368837838027643282775172273657572744784112294389733810861607423253291974813120197604178281965697475898164531258434135959862784130128185406283476649088690521047580882615823961985770122407044330583075869039319604603404973156583208672105913300903752823415539745394397715257455290510212310947321610753474825740775273986348298498340756937955646638621874569499279016572103701364433135817214311791398222983845847334440270964182851005072927748364550578634501100852987812389473928699540834346158807043959118985815145779177143619698728131459483783202081474982171858011389071228250905826817436220577475921417653715687725614904582904992461028630081535583308130101987675856234343538955409175623400844887526162643568648833519463720377293240094456246923254350400678027273837755376406726898636241037491410966718557050759098100246789880178271925953381282421954028302759408448955014676668389697996886241636313376393903373455801407636741877711055384225739499110186468219696581651485130494222369947714763069155468217682876200362777257723781365331611196811280792669481887201298643660768551639860534602297871557517947385246369446923087894265948217008051120322365496288169035739121368338393591756418733850510970271613915439590991598154654417336311656936031122249937969999226781732358023111862644575299135758175008199839236284615249881088960232244362173771618086357015468484058622329792853875623486556440536962622018963571028812361567512543338303270029097668650568557157505516727518899194129711337690149916181315171544007728650573189557450920330185304847113818315407324053319038462084036421763703911550639789000742853672196280903477974533320468368795868580237952218629120080742819551317948157624448298518461509704888027274721574688131594750409732115080498190455803416826949787141316063210686391511681774304792596709376
> > >
> > > KeyboardInterrupt
> > >
> > > KeyboardInterrupt
> > >
> > > KeyboardInterrupt
> > >
> > > KeyboardInterrupt
> > >
> > > #roundoff
> > > result = 1/3.0
> > > result
> > > 0.3333333333333333
> > > result[0:3]
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: 'float' object is not subscriptable
> > > result(0:3)
> > > File "<stdin>", line 1

    result(0:3)
            ^

SyntaxError: invalid syntax

> > > repr('chai')
> > > "'chai'"
> > > str('chai')
> > > 'chai'
> > > print('chai')
> > > chai
> > >
> > > #comparison
> > >
> > > 1 < 2
> > > True
> > > 1 < 0
> > > False
> > > 8 = 8
> > > File "<stdin>", line 1

    8 = 8
    ^

SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

> > > 8 == 8
> > > True
> > > 8 == 8 == 8
> > > True
> > > 8 = 8
> > > File "<stdin>", line 1

    8 = 8
    ^

SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?

> > > 8 = 8 =8
> > > File "<stdin>", line 1

    8 = 8 =8
    ^

SyntaxError: cannot assign to literal

> > > 5.0 == 5.0
> > > True
> > > 4.0 != 5.0
> > > True
> > > x,y,z
> > > (2, 3, 4)
> > > x < y <z
> > > True
> > > x < y and y < z
> > > True
> > > x < y and y > z
> > > False
> > > x > y and y > z  
> > > False
> > > x > y  
> > > False
> > > x < y or y > z  
> > > True
> > > 1 == 2 < 3
> > > False
> > > #for more explain
> > > 1 == 2 and 2<3
> > > False
> > >
> > > #math operator
> > >
> > > import math
> > > math.floor(3.5)
> > > 3
> > > math.floor(-3.5)
> > > -4
> > >
> > > # trunc always go towards zero
> > >
> > > math.trunc(2.8)
> > > 2
> > > math.trunc(3.8)
> > > 3
> > > math.trunc(4.8)
> > > 4
> > > math.trunc(-4.8)
> > > -4
> > > math.trunc(-3.8)
> > > -3
> > >
> > > 9999999999999999999999999 + 1
> > > 10000000000000000000000000
> > > 9999999999999999999999999 \* 2.1
> > > 2.1000000000000003e+25
> > > 2 \*\* 200  
> > > 1606938044258990275541962092341162602522202993782792835301376
> > >
> > > #octal liter
> > > 0o20
> > > 16
> > > #octal literal denote with [0o]
> > > #for hexal litteral denote with [0x]
> > > 0oFF
> > > File "<stdin>", line 1

    0oFF
     ^

SyntaxError: invalid octal literal

> > > 0xFF
> > > 255
> > > ob1000 # binary
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'ob1000' is not defined
> > > ob1000  
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'ob1000' is not defined
> > > ob1000
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'ob1000' is not defined
> > > 0xFF
> > > 255
> > > 0b1000
> > > 8
> > > oct(64)
> > > '0o100'
> > > hex(64)
> > > '0x40'
> > > bin(64)
> > > '0b1000000'
> > >
> > > int(3.14)
> > > 3
> > > int(64)  
> > > 64
> > > int('64', 8)
> > > 52
> > > #octal vlue by int
> > > int('64', 8)  
> > > 52
> > > int('10000',2)  
> > > KeyboardInterrupt
> > >
> > > # binary value by int
> > >
> > > int('10000',2)  
> > > 16
> > > int('1000',2)  
> > > 8
> > > #bitwise operator
> > >
> > > x = 1
> > > #left shift by two bits
> > > x << 2
> > > 4
> > > x | 2
> > > 3
> > >
> > > #random import
> > >
> > > import random
> > > random.random()
> > > 0.9373163943098486
> > > random.random()
> > > 0.5585556421561568
> > > random.random()
> > > 0.39456800970712913
> > > random.random()
> > > 0.2944323415552711
> > > random.random()
> > > 0.04151948763250812
> > > random.random()
> > > 0.6756839554744609
> > > random.random()
> > > 0.9999624551003503
> > > random.random()
> > > 0.8719875292648545
> > > random.random()
> > > 0.869199195898852
> > > random.random()
> > > 0.589205915518724
> > > random.random()*10
> > > 8.302410437603173
> > > random.random()*10
> > > 6.677124614531849
> > > random.randint(1,100)
> > > 2
> > > random.randint(1,100)
> > > 28
> > > random.randint(1,100)
> > > 80
> > > random.randint(1,100)
> > > 1
> > > random.randint(1,100)
> > > 41
> > >
> > > l1 = ['lemon','masala','ginger','mint']
> > > random.choice(l1)
> > > 'mint'
> > > random.choice(l1)
> > > 'masala'
> > > random.choice(l1)
> > > 'masala'
> > > l1 = ['lemon','masala','ginger','mint']
> > > random.choice(l1)
> > > 'ginger'
> > > random.choice(l1)
> > > 'lemon'
> > > random.choice(l1)
> > > 'mint'
> > > random.choice(l1)
> > > 'mint'
> > >
> > > random.shuffle(l1)
> > > l1
> > > ['masala', 'lemon', 'mint', 'ginger']
> > > l1
> > > ['masala', 'lemon', 'mint', 'ginger']
> > > l1
> > > ['masala', 'lemon', 'mint', 'ginger']
> > > l1
> > > ['masala', 'lemon', 'mint', 'ginger']
> > > l1
> > > ['masala', 'lemon', 'mint', 'ginger']
> > > random.shuffle(l1)
> > > l1
> > > ['lemon', 'masala', 'mint', 'ginger']
> > > l1
> > > ['lemon', 'masala', 'mint', 'ginger']
> > > l1
> > > ['lemon', 'masala', 'mint', 'ginger']
> > > l1
> > > ['lemon', 'masala', 'mint', 'ginger']
> > > l1
> > > ['lemon', 'masala', 'mint', 'ginger']
> > > random.shuffle(l1)
> > > l1
> > > ['masala', 'ginger', 'lemon', 'mint']
> > > 0.1 + 0.1 + 0.4
> > > 0.6000000000000001
> > > 0.1 + 0.1 + 0.1
> > > 0.30000000000000004
> > > 0.1 + 0.1 + 0.1 - 0.3
> > > 5.551115123125783e-17
> > > (0.1 + 0.1 + 0.1) - 0.3
> > > 5.551115123125783e-17
> > > from decimal import Decimal
> > > Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
> > > Decimal('0.0')
> > > Decimal('0.1') + Decimal('0.1') + Decimal('0.1')  
> > > Decimal('0.3')
> > >
> > > #for fraction
> > >
> > > from fraction import Fraction
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > ModuleNotFoundError: No module named 'fraction'
> > > from fractions import Fraction
> > > myFra = Fraction(2,7)
> > > myFra
> > > Fraction(2, 7)
> > >
> > > #setone
> > >
> > > setone = {1,2,3,4}
> > > setone _ 2
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: unsupported operand type(s) for _: 'set' and 'int'
> > > setone & {1,3}
> > > {1, 3}
> > >
> > > # upper one is intersection and it is denotedby empercent (&)
> > >
> > > setone | {1,3}
> > > {1, 2, 3, 4}
> > > setone | {1,317}
> > > {1, 2, 3, 4, 317}
> > > setone - {1,2,3,4}
> > > set()
> > > set
> > > <class 'set'>
> > > seone
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > NameError: name 'seone' is not defined. Did you mean: 'setone'?
> > > setone()
> > > Traceback (most recent call last):
> > > File "<stdin>", line 1, in <module>
> > > TypeError: 'set' object is not callable
> > > set()
> > > set()
> > > type({})
> > > <class 'dict'>
> > > #for unique camparison of set [ | ]
> > >
> > > type(True)
> > > <class 'bool'>
> > >
> > > True == 1
> > > True
> > > False == 0
> > > True
> > > True is 1
> > > <stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
> > > False
> > > True + 4
> > > 5
