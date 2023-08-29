#Sistema de Ecuaciones
a=int(input("ingrese numero: "))
b=int(input("ingrese numero: "))
c=int(input("ingrese numero: "))
d=int(input("ingrese numero: "))
e=int(input("ingrese numero: "))
f=int(input("ingrese numero: "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det
   
    print("x=",x)
    print("y=",y)