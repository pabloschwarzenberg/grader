a11 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
a12 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
b1 = float(input("Ingrese el resultado de la primera ecuación: "))
a21 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
a22 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
b2 = float(input("Ingrese el resultado de la segunda ecuación: "))

det = a11*a22 - a12*a21
if det == 0:
    print("El sistema no tiene solución")
else:
    x = (a22*b1 - a12*b2)/det
    y = (a11*b2 - a21*b1)/det

print("Las soluciones son x = ", round(x, 1),"e y = ", round(y, 1))