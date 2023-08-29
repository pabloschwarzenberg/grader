def solve_equation(a, b, c, d, e, f):

    det = a * e - b * d
    if det == 0:
        return None  

    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    return x, y

a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término constante de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término constante de la segunda ecuación: "))

solutions = solve_equation(a, b, c, d, e, f)

if solutions is not None:
    x = round(solutions[0], 1)
    y = round(solutions[1], 1)
    print("x =", x)
    print("y =",  y)
else:
    print("El sistema no tiene solución única.")
