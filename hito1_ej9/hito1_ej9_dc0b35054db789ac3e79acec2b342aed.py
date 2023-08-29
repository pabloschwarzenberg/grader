#Sistema de Ecuaciones
a = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

print("La solución del sistema es:")
print("x =", round(x, 1))
print("y =", round(y, 1))     