def solve_equations(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        return None  # El sistema no tiene solución única

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return x, y

a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

solution = solve_equations(a1, b1, c1, a2, b2, c2)

if solution is None:
    print("El sistema no tiene solución única.")
else:
    x, y = solution
    print("x =", round(x, 1))
    print("y =", round(y, 1))

