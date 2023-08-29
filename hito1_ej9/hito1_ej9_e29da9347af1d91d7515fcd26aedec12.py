import numpy as np

def resolver_sistema(a1, b1, c1, a2, b2, c2):
    coeficientes = np.array([[a1, b1], [a2, b2]])
    constantes = np.array([c1, c2])
    soluciones = np.linalg.solve(coeficientes, constantes)
    return soluciones

# Ejemplo de uso
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)
x = round(soluciones[0], 1)
y = round(soluciones[1], 1)

print("La solución del sistema es:")
print("x =", x)
print("y =", y)
