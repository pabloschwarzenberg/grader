#Sistema de Ecuaciones
# Pedimos al usuario que ingrese los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Calculamos la solución del sistema de ecuaciones
x = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
y = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

# Imprimimos las soluciones redondeadas a un decimal
print("x = {:.1f}".format(x))
print("y = {:.1f}".format(y))