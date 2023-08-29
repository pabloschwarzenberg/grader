#Sistema de Ecuaciones
a=int(input("Ingrese A "))
b=int(input("Ingrese B "))
c=int(input("Ingrese C "))
d=int(input("Ingrese D "))
e=int(input("Ingrese E "))
f=int(input("Ingrese F "))

det = a * e - b * d

if det==0:
    print("El sistema no se puede resolver ")
else:
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print("x= "+str(x)+"")
    print("y= "+str(y)+"")