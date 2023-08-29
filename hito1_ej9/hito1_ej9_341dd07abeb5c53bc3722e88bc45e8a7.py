#Sistema de Ecuaciones
a=float(input("Ingresa un número: "))
b=float(input("Ingresa un número: "))
c=float(input("Ingresa un número: "))
d=float(input("Ingresa un número: "))
e=float(input("Ingresa un número: "))
f=float(input("Ingresa un número: "))

det=a*e - b*d
if det!= 0:
    x= (c*e - b*f)/det
    y= (a*f - c*d)/det
print("x=",x)
print("y=",y)

     