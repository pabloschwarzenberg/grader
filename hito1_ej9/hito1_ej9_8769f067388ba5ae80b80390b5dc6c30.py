#Sistema de Ecuaciones
print("Ingresa los valres de las ecuaciones: ")
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
determinante = a*e - b*d
if determinante != 0:
    x = (c*e - b*f) / determinante
    y = (a*f - c*d) / determinante
else:
    x = None
    y = None
print("x=",x, "y=",y, end="")