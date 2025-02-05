#leap year
#hint: a leap year is divisible by 4,except for years that are divisible by 100 but not divisible by 400

year = int(input("enter a year:"))

leap = False


if year%100 == 0 and year%400 != 0:
    leap = False
elif year%4 ==0:
    leap = True
else: 
    leap = False

print(leap)
