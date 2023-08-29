#Sistema de Ecuaciones
print("Ingrese los datos para el siguiente tipo de ecuacion: ax + by = c")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
#Sistema de ecuaciones v2
print("Ahora ingresa los datos de una nueva ecuacion: dx + ey = f")
d = float(input("Ingrese el valor de d: "))
e = float(input("Ingrese el valor de e: "))
f = float(input("Ingrese el valor de f: "))

#Condicionante para evitar error
if (a*e - b*d) == 0:
    print("0")

else:
#Formula sistema de ecuaciones
    m = (a*e - b*d)
    x = (e*c - f*b) / m
    y = (f*a - d*c) / m

#Print apropiado para una solucion pertinente  
    print("x=",x,sep="")
    print("y=",y,sep="")