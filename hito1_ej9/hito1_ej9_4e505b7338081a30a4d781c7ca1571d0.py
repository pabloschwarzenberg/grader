#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return (x, y)

# Ejemplo de uso del programa
a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)
if solucion is None:
    print("El sistema no tiene solución")
else:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
      