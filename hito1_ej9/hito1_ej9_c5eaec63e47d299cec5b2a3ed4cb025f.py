   import numpy as np

def resolver_sistema(a, b, c, d, e, f):
    # Construir la matriz de coeficientes
    coeficientes = np.array([[a, b], [c, d]])

    # Construir el vector de términos independientes
    terminos_independientes = np.array([e, f])

    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(coeficientes, terminos_independientes)

    return solucion

# Obtener los coeficientes del sistema de ecuaciones
a = float(input("Coeficiente de x en la primera ecuación: "))
b = float(input("Coeficiente de y en la primera ecuación: "))
c = float(input("Coeficiente de x en la segunda ecuación: "))
d = float(input("Coeficiente de y en la segunda ecuación: "))
e = float(input("Término independiente de la primera ecuación: "))
f = float(input("Término independiente de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
x = round(soluciones[0], 1)
y = round(soluciones[1], 1)

print("x =", x)
print("y =", y)
   