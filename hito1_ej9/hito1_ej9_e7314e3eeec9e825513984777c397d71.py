#Sistema de Ecuaciones
a=float(input("ingrese un valor a: "))
b=float(input("ingrese un valor b: "))
c=float(input("ingrese un valor c: "))
d=float(input("ingrese un valor d: "))
e=float(input("ingrese un valor e: "))
f=float(input("ingrese un valor f: "))

x=(f*b-e*c)/(d*b-e*a)
y=(f*a-d*c)/(e*a-d*b)

print("x=",x)
print("y=",y)