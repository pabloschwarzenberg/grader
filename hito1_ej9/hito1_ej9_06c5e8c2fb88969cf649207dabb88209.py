#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (b2 * c1 - b1 * c2) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        print("Las soluciones son:")
        print("x =", round(x, 1))
        print("y =", round(y, 1))


# Obtener los coeficientes del usuario
a1 = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c1 = float(input("Ingrese el coeficiente 'c' de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente 'a' de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente 'b' de la segunda ecuación: "))
c2 = float(input("Ingrese el coeficiente 'c' de la segunda ecuación: "))

# Resolver el sistema
resolver_sistema(a1, b1, c1, a2, b2, c2)