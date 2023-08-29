#Sistema de Ecuaciones
def resolver_sistema_ecuaciones(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante != 0:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        print("x =", round(x, 1))
        print("y =", round(y, 1))
    else:
        print("El sistema no tiene solución única.")

a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

resolver_sistema_ecuaciones(a1, b1, c1, a2, b2, c2)