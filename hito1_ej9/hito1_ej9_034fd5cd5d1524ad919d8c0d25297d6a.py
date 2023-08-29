a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

det = a1*b2 - a2*b1

if det == 0:
    print("El sistema no tiene solución")
else:

    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    print("x = {:.1f}".format(x))
    print("y = {:.1f}".format(y))
      