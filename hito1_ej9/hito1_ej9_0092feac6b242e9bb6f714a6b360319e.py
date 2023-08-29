def resolver_sistema():
    a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
    b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
    c1 = float(input("Ingrese la constante de la primera ecuación: "))
    a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
    b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
    c2 = float(input("Ingrese la constante de la segunda ecuación: "))

    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única")
        return

    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    print("x =", round(x, 1))
    print("y =", round(y, 1))

# Ejemplo de uso
print("Resolución de un sistema de ecuaciones lineales con dos incógnitas.")
resolver_sistema()


      