# finding factorial for any number by using loops

n  = int(input("enter a number:"))

factorial = 1

while n>0:
    factorial = factorial*n
   
    n = n-1 # n -=1

print(factorial)