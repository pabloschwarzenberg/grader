import numpy as np

# Obtener los coeficientes del sistema de ecuaciones
a11 = float(input("Ingrese el coeficiente a11: "))
a12 = float(input("Ingrese el coeficiente a12: "))
b1 = float(input("Ingrese el término independiente b1: "))

a21 = float(input("Ingrese el coeficiente a21: "))
a22 = float(input("Ingrese el coeficiente a22: "))
b2 = float(input("Ingrese el término independiente b2: "))

# Crear las matrices del sistema de ecuaciones
A = np.array([[a11, a12], [a21, a22]])
B = np.array([b1, b2])

# Resolver el sistema de ecuaciones
soluciones = np.linalg.solve(A, B)

# Imprimir las soluciones redondeadas a un decimal
x1 = round(soluciones[0], 1)
x2 = round(soluciones[1], 1)
print("Las soluciones son:")
print(f"x1 = {x1}")
print(f"x2 = {x2}")
a11 * x1 + a12 * x2 = b1
a21 * x1 + a22 * x2 = b2
