#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    denominador = a1 * b2 - a2 * b1

    if denominador == 0:
        return None  # No hay solución única

    x = (b2 * c1 - b1 * c2) / denominador
    y = (a1 * c2 - a2 * c1) / denominador

    return x, y

# Solicitar los coeficientes y constantes del sistema al usuario
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese la constante de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese la constante de la segunda ecuación: "))

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

if soluciones is not None:
    x, y = soluciones
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
