def solve_system(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        return None  # El sistema no tiene solución única
    x = (e * d - b * f) / determinant
    y = (a * f - c * e) / determinant
    return x, y

# Solicitar los valores del sistema al usuario
a = float(input("Ingrese el valor de x1: "))
b = float(input("Ingrese el valor de y1: "))
e = float(input("Ingrese el valor de resultado1: "))
c = float(input("Ingrese el valor de x2: "))
d = float(input("Ingrese el valor de y2: "))
f = float(input("Ingrese el valor de resultado2: "))

# Resolver el sistema
solutions = solve_system(a, b, c, d, e, f)

if solutions is None:
    print("El sistema no tiene solución única.")
else:
    # Redondear las soluciones a un decimal
    x = round(solutions[0], 1)
    y = round(solutions[1], 1)
    print("Las soluciones del sistema son: x = ",x," y = ",y)