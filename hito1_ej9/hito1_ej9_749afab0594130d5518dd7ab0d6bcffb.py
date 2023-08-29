#Sistema de Ecuaciones
import numpy as np

def solve_equations(a1, b1, c1, a2, b2, c2):
    coefficients = np.array([[a1, b1], [a2, b2]])
    constants = np.array([c1, c2])
    solutions = np.linalg.solve(coefficients, constants)
    x = round(solutions[0], 1)
    y = round(solutions[1], 1)
     print(f'x={x}')
     print(f'y={y}')
    
# Ejemplo de uso
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5
solve_equations(a1, b1, c1, a2, b2, c2)
