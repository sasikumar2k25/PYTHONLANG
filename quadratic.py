#input a,b,c
a = int(input("give a vale a:"))
b = int(input("give a vale b:"))
c = int(input("give a vale c:"))
d = (b**2)-4*a*c
root1 = 0
root2 = 0
root1 = (-b + (d**(0.5)))/2*a
root1 = (-b - (d**(0.5)))/2*a
print(f"roots:({root1},{root2})")
