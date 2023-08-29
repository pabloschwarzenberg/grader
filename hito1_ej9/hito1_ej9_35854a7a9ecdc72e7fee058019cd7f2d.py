def solve_system(a, b, c, d, e, f):
    determinant = a * e - b * d

    if determinant == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (c * e - b * f) / determinant
        y = (a * f - c * d) / determinant

        print("x = {:.1f}".format(x))
        print("y = {:.1f}".format(y))

# Pedir los valores al usuario
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))

d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Resolver el sistema
solve_system(a, b, c, d, e, f)