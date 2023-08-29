#Sistema de Ecuaciones
print("Sistema de Ecuaciones")
print("ax+by=c")
print("dx+ey=f")
a=float(input("Ingrese valor de a: "))
b=float(input("Ingrese valor de b: "))
c=float(input("Ingrese valor be c: "))
d=float(input("Ingrese valor be d: "))
e=float(input("Ingrese valor be e: "))
f=float(input("Ingrese valor be f: "))

y=(a*f-c*d)//(a*e-c*b)
x=(c-b*y)//a

print=("x=",x,"y=",y)