def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única.")
        return

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    print("x =", round(x, 1))
    print("y =", round(y, 1))


# Solicitar los coeficientes y términos independientes del sistema al usuario
a1 = float(input("Coeficiente de x en la primera ecuación: "))
b1 = float(input("Coeficiente de y en la primera ecuación: "))
c1 = float(input("Término independiente en la primera ecuación: "))
a2 = float(input("Coeficiente de x en la segunda ecuación: "))
b2 = float(input("Coeficiente de y en la segunda ecuación: "))
c2 = float(input("Término independiente en la segunda ecuación: "))

# Resolver el sistema
resolver_sistema(a1, b1, c1, a2, b2, c2)
