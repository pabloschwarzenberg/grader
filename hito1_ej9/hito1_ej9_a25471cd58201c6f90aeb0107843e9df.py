#Sistema de Ecuaciones
a=int(input("Ingrese su numero a: "))
b=int(input("Ingrese su numero b: "))
c=int(input("Ingrese su numero c: "))
d=int(input("Ingrese su numero d: "))
e=int(input("Ingrese su numero e: "))
f=int(input("Ingrese su numero f: "))

determinante= a*e - b*d

resulX=float(c*e - b*f)//determinante
resulY=float(a*f- c*d)//determinante

print("X=",resulX)
print("Y=",resulY)      