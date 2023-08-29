#Sistema de Ecuaciones
print("Escribir sistema de ecuaciones con 2 incognitas, tu programa recibira los 6 numeros reales que representan el sistema y imprimira las soluciones redondeadas a un decimal")
print("Ingrese los valores del sistema de la forma ax+by=c y dx+ey=f: ")
a = int(input("Ingrese valor a: "))
b = int(input("Ingrese valor b: "))
c = int(input("Ingrese valor c: "))
d = int(input("Ingrese valor d: "))
e = int(input("Ingrese valor e: "))
f = int(input("Ingrese valor f: "))
determinante = a*e - b*d

if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante
else:
    x = "None"
    y = "None"
print("x=",x)
print("y=",y)
