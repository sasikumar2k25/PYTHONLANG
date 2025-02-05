# palindrome -->means ex:MOM reverse is MOM ,121 reverse is 121

s = input("Give a string:")

reverse = s[::-1]

if reverse==s:
    print("It is a palindrome")
else :
    print("It's not a palindrome")