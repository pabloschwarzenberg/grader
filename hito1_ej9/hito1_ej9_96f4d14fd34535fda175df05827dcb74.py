def solve_system(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        print("El sistema no tiene solución única.")
        return
    else:
        x = (e * d - b * f) / determinant
        y = (a * f - c * e) / determinant
        return x, y

# Leer los valores del sistema
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
e = float(input("Ingrese el término constante de la primera ecuación: "))
c = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
d = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término constante de la segunda ecuación: "))

# Resolver el sistema
solutions = solve_system(a, b, c, d, e, f)

# Imprimir las soluciones redondeadas a un decimal
if solutions:
    print("x =", round(solutions[0], 1))
    print("y =", round(solutions[1], 1))







    