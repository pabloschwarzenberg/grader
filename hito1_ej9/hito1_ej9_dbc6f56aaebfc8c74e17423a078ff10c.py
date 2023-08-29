#Sistema de Ecuaciones
a=int(input("ingrese valor de a: "))
b=int(input("ingrese valor de b: "))
c=int(input("ingrese valor de c: "))
d=int(input("ingrese valor de d: "))
e=int(input("ingrese valor de e: "))
f=int(input("ingrese valor de f: "))

disk= a*e-b*d
x=(c*e-b*f)/disk
y=(a*f-c*d)/disk

round(x,1)
round(y,1)
print("x=",x)
print("y=",y)