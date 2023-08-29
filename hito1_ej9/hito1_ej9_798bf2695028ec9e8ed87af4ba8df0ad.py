#Sistema de Ecuaciones
a = float(input("Ingresa el coeficiente de x de la primera ecuación: "))
b = float(input("Ingresa el coeficiente de y de la primera ecuación: "))
c = float(input("Ingresa el término independiente de la primera ecuación: "))
d = float(input("Ingresa el coeficiente de x de la segunda ecuación: "))
e = float(input("Ingresa el coeficiente de y de la segunda ecuación: "))
f = float(input("Ingresa el término independiente de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# Imprimir el resultado
print("x =", round(x, 1))
print("y =", round(y, 1))   