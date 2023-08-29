#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None, None  # No hay solución única

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    return x, y

# Solicitar al usuario los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

# Resolver el sistema de ecuaciones
solucion_x, solucion_y = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Imprimir las soluciones redondeadas a un decimal
if solucion_x is None:
    print("No hay solución única para el sistema de ecuaciones.")
else:
    print("x =", round(solucion_x, 1))
    print("y =", round(solucion_y, 1))      