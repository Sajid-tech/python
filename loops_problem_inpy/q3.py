input = int(input("Which number you want to make the table: "))

for i in range(1,11):
    if (i == 5):
        continue
    print(input, 'x', i, '=', input*i)



