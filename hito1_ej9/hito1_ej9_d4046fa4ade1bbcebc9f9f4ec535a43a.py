#Sistema de Ecuaciones
import numpy as np

def resolver_sistema(a, b, c, d, e, f):
    coeficientes = np.array([[a, b], [c, d]])
    constantes = np.array([e, f])
    soluciones = np.linalg.solve(coeficientes, constantes)
    return soluciones

# Solicitar los coeficientes del sistema al usuario
a = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
e = float(input("Ingrese el resultado de la primera ecuación: "))
c = float(input("Ingrese el coeficiente 'a' de la segunda ecuación: "))
d = float(input("Ingrese el coeficiente 'b' de la segunda ecuación: "))
f = float(input("Ingrese el resultado de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
x = round(soluciones[0], 1)
y = round(soluciones[1], 1)
print(f"Las soluciones del sistema son: x = {x}, y = {y}")
