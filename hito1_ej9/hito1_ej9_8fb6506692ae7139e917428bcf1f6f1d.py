def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return "El sistema no tiene solución única."

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return "x = {}\ny = {}".format(round(x, 1), round(y, 1))


# Interacción con el usuario
print("Ingrese los coeficientes del sistema de ecuaciones:")
a1 = float(input("Coeficiente de x en la primera ecuación: "))
b1 = float(input("Coeficiente de y en la primera ecuación: "))
c1 = float(input("Constante en la primera ecuación: "))
a2 = float(input("Coeficiente de x en la segunda ecuación: "))
b2 = float(input("Coeficiente de y en la segunda ecuación: "))
c2 = float(input("Constante en la segunda ecuación: "))

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)
print(soluciones)
