#Sistema de Ecuaciones
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese la constante de la primera ecuación: "))

d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese la constante de la segunda ecuación: "))

denominador = a * e - b * d
x = (c * e - b * f) / denominador
y = (a * f - c * d) / denominador

x = round(x, 1)
y = round(y, 1)

print("Las soluciones son:")
print("x =", x)
print("y =", y)     