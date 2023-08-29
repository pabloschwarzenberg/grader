#Sistema de Ecuaciones
import numpy as np

def resolver_sistema(a, b, c, d, e, f):
    matriz_coeficientes = np.array([[a, b], [c, d]])
    vector_soluciones = np.array([e, f])
    soluciones = np.linalg.solve(matriz_coeficientes, vector_soluciones)
    x = round(soluciones[0], 1)
    y = round(soluciones[1], 1)
    return x, y

# Ejemplo de uso
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

x, y = resolver_sistema(a, b, c, d, e, f)

print(f'x = {x}')
print(f'y = {y}')