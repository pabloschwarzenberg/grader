#Sistema de Ecuaciones
a = float(input("Ingresa el coeficiente de x en la primera ecuación: "))
b = float(input("Ingresa el coeficiente de y en la primera ecuación: "))
c = float(input("Ingresa el término independiente de la primera ecuación: "))
d = float(input("Ingresa el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingresa el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingresa el término independiente de la segunda ecuación: "))

x = (c * e - b * f) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

print("x =", round(x, 1))
print("y =", round(y, 1))
