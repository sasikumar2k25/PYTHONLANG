# sum of natural numbers 

n = int(input("enter a number:"))


i = 1

sum =0
while i<=n:
    sum = i  + sum
    i  +=1
    print("sum of first 5 natural number:",sum)