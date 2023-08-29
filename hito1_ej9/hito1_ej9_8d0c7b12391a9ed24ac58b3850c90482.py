#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

# Solicitar al usuario los coeficientes y constantes del sistema
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese la constante en la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese la constante en la segunda ecuación: "))

# Resolver el sistema
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Imprimir las soluciones redondeadas a un decimal
if soluciones is None:
    print("El sistema no tiene solución única")
else:
    x = round(soluciones[0], 1)
    y = round(soluciones[1], 1)
    print("Las soluciones son: x =", x, "y =", y)
