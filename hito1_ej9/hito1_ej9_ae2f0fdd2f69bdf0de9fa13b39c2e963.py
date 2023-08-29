#Sistema de Ecuaciones
a=int(input("ingrese el numero: "))
b=int(input("ingrese el numero: "))
c=int(input("ingrese el numero: "))
d=int(input("ingrese el numero: "))
e=int(input("ingrese el numero: "))
f=int(input("ingrese el numero: "))
det = a * e - b * d
if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det   
    print("x=",x)
    print("y=",y)      