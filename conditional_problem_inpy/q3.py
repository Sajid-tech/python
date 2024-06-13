score = int(input("What is your score: "))

if score >= 101: 
    print("Please verify your grade again")
    exit()

# if ( score >=90 ):
#     print("your grade is 'A' ")
# elif (score >=80 ):
#     print("YOur score is 'B'")
# elif (score>= 70):
#     print("YOur score is 'C'")
# elif (score>= 60):
#     print("YOur score is 'D'")
# else:
#     print("your score is 'F'")

# or 

if ( score >=90 ):
    grade = 'A'
elif (score >=80 ):
    grade = 'B'
elif (score>= 70):
    grade ='C'
elif (score>= 60):
    grade ='D'
else:
    grade ='F'

print("grade:",grade)

