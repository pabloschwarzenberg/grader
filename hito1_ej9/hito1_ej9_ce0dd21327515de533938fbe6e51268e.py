def solve_system(a, b, c, d, e, f):
    # Calcular determinante
    det = a * d - b * c

    # Calcular soluciones
    x = (d * e - b * f) / det
    y = (a * f - c * e) / det

    # Redondear las soluciones a un decimal
    x_rounded = round(x, 1)
    y_rounded = round(y, 1)

    return ['x=' + str(x_rounded), 'y=' + str(y_rounded)]

# Obtener los coeficientes del sistema de ecuaciones
coefficients = input("Ingrese los coeficientes 'a', 'b', 'c', 'd', 'e' y 'f', separados por espacios: ").split()
a, b, c, d, e, f = map(float, coefficients)

solution = solve_system(a, b, c, d, e, f)
print("Las soluciones son:")
for s in solution:
    print(s)
