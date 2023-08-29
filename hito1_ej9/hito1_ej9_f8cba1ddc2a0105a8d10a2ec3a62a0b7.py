#Sistema de Ecuaciones
a11 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
a12 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
b1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a21 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
a22 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
b2 = float(input("Ingrese el término independiente de la segunda ecuación: "))
factor = a21/a11
a21 = a21 - factor * a11
a22 = a22 - factor * a12
b2 = b2 - factor * b1
y = b2 / a22
x = (b1 - a12 * y) / a11
print("x = {:.1f}".format(x))
print("y = {:.1f}".format(y))