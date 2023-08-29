# Pedimos al usuario los coeficientes del sistema
a1 = float(input("Introduce el coeficiente de x de la primera ecuación: "))
b1 = float(input("Introduce el coeficiente de y de la primera ecuación: "))
c1 = float(input("Introduce el término independiente de la primera ecuación: "))
a2 = float(input("Introduce el coeficiente de x de la segunda ecuación: "))
b2 = float(input("Introduce el coeficiente de y de la segunda ecuación: "))
c2 = float(input("Introduce el término independiente de la segunda ecuación: "))

# Resolvemos el sistema por el método de sustitución
y = (c2 - a2 * c1 / a1) / (b2 - a2 * b1 / a1)
x = (c1 - b1 * y) / a1

# Imprimimos las soluciones redondeadas a un decimal
print("x = {:.1f}".format(x))
print("y = {:.1f}".format(y))