import numpy as np

# Leer los coeficientes y los términos constantes del sistema
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término constante de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término constante de la segunda ecuación: "))

# Construir la matriz de coeficientes y el vector de términos constantes
A = np.array([[a1, b1], [a2, b2]])
B = np.array([c1, c2])

# Resolver el sistema de ecuaciones
soluciones = np.linalg.solve(A, B)

# Imprimir las soluciones redondeadas a un decimal
print(f"x = {soluciones[0]:.1f}")
print(f"y = {soluciones[1]:.1f}")
