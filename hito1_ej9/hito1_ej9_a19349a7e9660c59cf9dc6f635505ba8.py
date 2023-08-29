a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
a3 = float(input("Ingrese la constante en la primera ecuación: "))

b1 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
b3 = float(input("Ingrese la constante en la segunda ecuación: "))


determinante = a1 * b2 - b1 * a2

if determinante == 0:
    print("El sistema no tiene solución única.")
else:
    x = (a3 * b2 - b3 * a2) / determinante
    y = (a1 * b3 - b1 * a3) / determinante

    print("x =", round(x, 1))
    print("y =", round(y, 1))