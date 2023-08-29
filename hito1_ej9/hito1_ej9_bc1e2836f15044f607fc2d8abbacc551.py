#Sistema de Ecuaciones
a=float(input("A: "))
b=float(input("B: "))
c=float(input("C: "))
d=float(input("D: "))
e=float(input("E: "))
f=float(input("F: "))
y=(f*a-c*d)/(e*a-b*d)
x=(f-e*y)/d
print("x=",x)
print("y=",y)