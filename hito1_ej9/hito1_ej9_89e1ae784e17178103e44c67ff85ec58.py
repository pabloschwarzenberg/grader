#Sistema de Ecuaciones
a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
c=float(input("Ingrese c: "))
d=float(input("Ingrese d: "))
e=float(input("Ingrese e: "))
f=float(input("Ingrese f: "))
y=(f*a-d*c)/(a*e-d*b)
x=(c-b*y)/a
print("x=",x)
print("y=",y)