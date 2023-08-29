#Sistema de Ecuaciones
def solve_system(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (e * d - b * f) / determinant
        y = (a * f - c * e) / determinant
        print("x = {:.1f}".format(x))
        print("y = {:.1f}".format(y))


# Ejemplo de uso con los valores proporcionados
solve_system(2, 3, 1, 2, 6, 5)
      