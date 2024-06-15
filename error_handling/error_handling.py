'''x = ('Masala','lemon','ginger')

y = enumerate(x)
#jitni bhi value ek baar bn jati hai toh phir aap usko list mein convert kr skte ho
print(list(y)) # list bani hai lein key value pair ki bni hai
#output : [(0, 'Masala'), (1, 'lemon'), (2, 'ginger')]

file  = open('test.py','w') # here 'w':write mode wil make file imediatly
'''

# enumarate add indexing in list tuple too
# try catch 

file = open('youtube.txt','w')

# used in file fandling always use 
try:
    file.write('chai or code')
finally: # finally means jitne bhi exception the vo ho gya ab bs finaally ye kaam kr do
    file.close()

# either do upper one or this one
with open('youtube.txt','w') as file: # its close the file automatically
    file.write('chai or python')