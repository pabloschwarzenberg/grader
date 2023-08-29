#Sistema de Ecuaciones
import numpy as np

def solve_equations(a1, b1, c1, a2, b2, c2):
    # Crear la matriz de coeficientes
    coefficients = np.array([[a1, b1], [a2, b2]])
    # Crear el vector de constantes
    constants = np.array([c1, c2])
    # Resolver el sistema de ecuaciones
    solutions = np.linalg.solve(coefficients, constants)
    # Redondear las soluciones a un decimal
    rounded_solutions = np.round(solutions, decimals=1)
    # Imprimir las soluciones
    print(f"x = {rounded_solutions[0]}")
    print(f"y = {rounded_solutions[1]}")

# Ejemplo de uso
solve_equations(2, 3, 6, 1, 2, 5)

      