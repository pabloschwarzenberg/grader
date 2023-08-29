#Sistema de Ecuaciones
a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c1 = float(input("Ingrese la constante de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Ingrese la constante de la segunda ecuación: "))

determinante = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / determinante
y = (a1 * c2 - a2 * c1) / determinante


print("x =", round(x, 1))
print("y =", round(y, 1))
