import numpy as np

def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Crear una matriz de coeficientes
    coeficientes = np.array([[a1, b1], [a2, b2]])
    
    # Crear una matriz de constantes
    constantes = np.array([c1, c2])
    
    # Resolver el sistema de ecuaciones
    solucion = np.linalg.solve(coeficientes, constantes)
    
    return solucion

# Ejemplo de uso
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)
x = round(solucion[0], 1)
y = round(solucion[1], 1)

print(f"x = {x}")
print(f"y = {y}")
      