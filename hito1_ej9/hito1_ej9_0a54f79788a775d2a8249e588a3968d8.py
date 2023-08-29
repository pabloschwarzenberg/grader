#Sistema de Ecuaciones
a1 = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente 'a' de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente 'b' de la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

y = (c1 - a1 * c2 / a2) / (b1 - a1 * b2 / a2)

x = (c2 - b2 * y) / a2

print("x =", round(x, 1))
print("y =", round(y, 1))
