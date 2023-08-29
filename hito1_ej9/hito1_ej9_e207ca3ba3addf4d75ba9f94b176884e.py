import numpy as np

# Solicitar los coeficientes del sistema de ecuaciones
a1 = float(input("Coeficiente a1: "))
b1 = float(input("Coeficiente b1: "))
c1 = float(input("Coeficiente c1: "))
a2 = float(input("Coeficiente a2: "))
b2 = float(input("Coeficiente b2: "))
c2 = float(input("Coeficiente c2: "))

# Crear las matrices del sistema de ecuaciones
A = np.array([[a1, b1], [a2, b2]])
B = np.array([c1, c2])

# Resolver el sistema de ecuaciones
sol = np.linalg.solve(A, B)

# Obtener las soluciones redondeadas a un decimal
sol1 = round(sol[0], 1)
sol2 = round(sol[1], 1)

# Imprimir las soluciones
print("Solución x:", sol1)
print("Solución y:", sol2)

