a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el resultado de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el resultado de la segunda ecuación: "))

det = a1 * b2 - a2 * b1
det_x = c1 * b2 - c2 * b1
det_y = a1 * c2 - a2 * c1

if det != 0:
    x = det_x / det
    y = det_y / det
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
