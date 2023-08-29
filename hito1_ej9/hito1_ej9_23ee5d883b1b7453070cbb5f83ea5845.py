def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

# Lectura de los coeficientes del sistema
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

# Resolución del sistema
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Impresión de las soluciones
if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    x, y = soluciones
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")
