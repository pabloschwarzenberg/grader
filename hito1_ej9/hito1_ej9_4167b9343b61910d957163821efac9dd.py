#Sistema de ecuaciones
a11 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
a12 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
b1 = float(input("Ingrese el término independiente de la primera ecuación: "))

a21 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
a22 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
b2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

determinante = a11 * a22 - a12 * a21

if determinante != 0:
    x = (b1 * a22 - b2 * a12) / determinante
    y = (b2 * a11 - b1 * a21) / determinante

    x = round(x, 1)
    y = round(y, 1)

    print("x =", x)
    print("y =", y)
else:
    print("El sistema de ecuaciones no tiene solución única.")

