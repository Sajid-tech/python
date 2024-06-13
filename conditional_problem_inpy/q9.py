#leap Year Calender

leap_year = int(input("check wheather the year is leap or not: ")) % 4


if leap_year == 0:
    print("leap year")
else:
    print("NOt a leap year")  