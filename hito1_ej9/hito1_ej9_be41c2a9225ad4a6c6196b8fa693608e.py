# Obtener los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente a de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente b de la primera ecuación: "))
c1 = float(input("Ingrese el coeficiente c de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente a de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente b de la segunda ecuación: "))
c2 = float(input("Ingrese el coeficiente c de la segunda ecuación: "))

det = a1 * b2 - a2 * b1

if det == 0:
    print("El sistema de ecuaciones no tiene solución única.")
else:
    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det

    print("x =", round(x, 1))
    print("y =", round(y, 1))

