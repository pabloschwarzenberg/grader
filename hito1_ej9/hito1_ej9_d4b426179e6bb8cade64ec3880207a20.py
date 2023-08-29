def solve_equation(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        print("El sistema de ecuaciones no tiene solución única.")
        return

    x = round((b2 * c1 - b1 * c2) / determinant, 1)
    y = round((a1 * c2 - a2 * c1) / determinant, 1)

    print(f"x={x}")
    print(f"y={y}")

# Ejemplo de uso
solve_equation(2, 3, 6, 1, 2, 5)