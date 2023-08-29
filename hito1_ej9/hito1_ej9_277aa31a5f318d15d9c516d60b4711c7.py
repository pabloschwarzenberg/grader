#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None

    x = round((b2 * c1 - b1 * c2) / determinante, 1)
    y = round((a1 * c2 - a2 * c1) / determinante, 1)

    return x, y


a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    x, y = soluciones
    print("Las soluciones son:")
    print("x =", x)
    print("y =", y)
      