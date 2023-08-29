#Sistema de Ecuaciones
def solve_system(a, b, c, d, e, f):
    determinant = a * d - b * c

    if determinant == 0:
        print("El sistema no tiene solución única.")
        return

    x = (e * d - b * f) / determinant
    y = (a * f - c * e) / determinant

    x = round(x, 1)
    y = round(y, 1)

    print("x =", x)
    print("y =", y)


