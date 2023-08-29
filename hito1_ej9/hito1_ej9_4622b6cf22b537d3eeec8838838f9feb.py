def solve_equation_system(a, b, c, d, e, f):
    determinant = a * d - b * c

    if determinant == 0:
        # El sistema no tiene solución única
        return None

    x = (e * d - b * f) / determinant
    y = (a * f - c * e) / determinant

    return x, y

# Obtener los valores del sistema de ecuaciones desde el usuario
a = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
e = float(input("Ingrese el resultado 'e' de la primera ecuación: "))
c = float(input("Ingrese el coeficiente 'c' de la segunda ecuación: "))
d = float(input("Ingrese el coeficiente 'd' de la segunda ecuación: "))
f = float(input("Ingrese el resultado 'f' de la segunda ecuación: "))

solutions = solve_equation_system(a, b, c, d, e, f)

if solutions is None:
    print("El sistema no tiene solución única.")
else:
    # Imprimir las soluciones redondeadas a un decimal
    x = round(solutions[0], 1)
    y = round(solutions[1], 1)

    print("x =", x)
    print("y =", y)


