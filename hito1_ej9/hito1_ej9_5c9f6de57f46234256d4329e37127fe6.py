#Sistema de Ecuaciones
a=float(input("Ingrese a: "))
b=float(input("Ingrese b: "))
c=float(input("Ingrese c: "))
d=float(input("Ingrese d: "))
e=float(input("Ingrese e: "))
f=float(input("Ingrese f: "))
y=(c*d-a*f)/(b*d-a*e)
x=(c-b*y)/a
print("y=",y)
print("x=",x)
