#Sistema de Ecuaciones
a=int(input("Ingrese numero"))
b=int(input("Ingrese numero"))
c=int(input("Ingrese numero"))
d=int(input("Ingrese numero"))
e=int(input("Ingrese numero"))
f=int(input("Ingrese numero"))

y=(a*f - d*c)/(a*e-d*b)
x=(c-b*y)/a

print("x=", x)
print("y=", y)