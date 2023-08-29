# Obtén los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Resuelve el sistema de ecuaciones mediante el método de sustitución
y = (c1 - (a1/a2)*c2) / (b1 - (a1/a2)*b2)
x = (c1 - b1*y) / a1

# Imprime las soluciones
print("x =", round(x, 1))
print("y =", round(y, 1))
