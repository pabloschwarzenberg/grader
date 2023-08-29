#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None

    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return round(x, 1), round(y, 1)

# Pedir los valores del sistema al usuario
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el término independiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el término independiente c2: "))

# Resolver el sistema
solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Imprimir la solución
if solucion is not None:
    x, y = solucion
    print(f"x = {x}")
    print(f"y = {y}")
else:
    print("El sistema no tiene solución única.")
      