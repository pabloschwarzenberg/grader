#Sistema de Ecuaciones
from os import system
system("cls")

def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    
    if determinante == 0:
        return None  
    
    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante
    
    return x, y

a = float(input("Coeficiente de x en la primera ecuación: "))
b = float(input("Coeficiente de y en la primera ecuación: "))
c = float(input("Coeficiente de x en la segunda ecuación: "))
d = float(input("Coeficiente de y en la segunda ecuación: "))
e = float(input("Termino independiente de la primera ecuación: "))
f = float(input("Termino independiente de la segunda ecuación: "))

soluciones = resolver_sistema(a, b, c, d, e, f)

if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    x, y = soluciones
    print("x =", round(x, 1))
    print("y =", round(y, 1))
    