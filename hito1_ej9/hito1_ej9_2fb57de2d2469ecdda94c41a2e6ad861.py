#Sistema de Ecuaciones
a=float(input("x1: "))
b=float(input("y1: "))
c=float(input("c1: "))
d=float(input("x2: "))
e=float(input("y2: "))
f=float(input("c2: "))
x=(f*b-e*c)/(b*d-e*a)
y=(c-a*x)/b
print("x= ",x,"y= ", y)
