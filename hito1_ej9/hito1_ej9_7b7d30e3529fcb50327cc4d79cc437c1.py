#Sistema de Ecuaciones
import numpy as np

def solve_system(a, b, c, d, e, f):
    coefficients = np.array([[a, b], [c, d]])
    constants = np.array([e, f])
    solutions = np.linalg.solve(coefficients, constants)
    return solutions

# Ejemplo de uso
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

x, y = solve_system(a, b, c, d, e, f)
print("x = {:.1f}".format(x))
print("y = {:.1f}".format(y))
      