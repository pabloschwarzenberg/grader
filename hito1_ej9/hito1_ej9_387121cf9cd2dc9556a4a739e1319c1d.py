#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None  

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    return x, y

a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el resultado c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el resultado c2: "))

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    print("x =", round(soluciones[0], 1))
    print("y =", round(soluciones[1], 1))
