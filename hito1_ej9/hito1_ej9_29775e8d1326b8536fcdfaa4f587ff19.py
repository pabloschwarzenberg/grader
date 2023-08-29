import numpy as np

# Definir las ecuaciones en forma matricial
coeficientes = np.array([[2, 3], [1, 2]])
resultados = np.array([6, 5])

# Resolver el sistema de ecuaciones
soluciones = np.linalg.solve(coeficientes, resultados)

# Imprimir las soluciones redondeadas a un decimal
x = round(soluciones[0], 1)
y = round(soluciones[1], 1)
print(f'x = {x}')
print(f'y = {y}')
