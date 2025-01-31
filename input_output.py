#input and output rule

#for variable input
'''
name = input("Enter your name :")
print("I am ",name)



#for integer input
number = int(input("enter your luky number here :"))
print("your lucky number is :",number)
print(type(number))

'''

#combination of variable and integer
'''
name = input("enter your name here :")
age = int (input("enter your age here :") )
print("Hello! everyone i am " +  name  +  "and im " , age,"years old.")

'''
#for float input
''''
weight_str = float(input("enter a float value:"))
print(type(weight_str))
'''
"""
#example for int,float,complex
a= 66482946
b= 86548.6248
c= 35j
print(type(a))
print(type(b))
print(type(c))

"""
'''
a=4444445
b=838
print(a, b ,sep="-" ,end=" so the program upto now ended here")

'''
#Example 1:-
'''
name = input("enter your name:" )
print("Hello",name,sep=", ",end="!")
'''
#Example 2:-
'''
num = int(input("enter a number:"))
print("You entered",num,sep=":")
'''
#Example 3:-
'''
float = float(input("enter a float value:"))
print("Value of Pi",float,sep=":")
'''
#Example 4:-
'''
a = input()
x,y,z = a.split(" ")
sum = int(x)+int(y)+int(z)

print(sum)
'''
#example 5:-
''''
 # "John",25

a = input("enter your name and age: ")
name,age = a.split(",")
print("Name:",name,",age:",age,sep="")
'''
#example 6:-
'''
a = int(input('enter a number:'))
print("countdowm:5 4 3 2 1 ",end="Blast off!")
'''
#example 7:- 
'''
r,s = input("enter a and b values: ").split(",")
a = int(r)
b = int(s)
print("addition:",a+b,"subtraction:",a-b,"multiplication:",a*b,"division:",a/b,sep=",")
'''
#example 8:-
''''
a = 10
b = 5
print("10>5:",a>b,",10<5:",a<b,",10==5:",a==b,",10!=5:",a!=b,sep="")
'''
#example 11:-
# Formatted (f)
x,y = input("enter your name and age:").split(",")
print(f"Name:{x},age:{y}years")