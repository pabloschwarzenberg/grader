#Sistema de Ecuaciones
a = float(input("Ingrese el coeficiente de x en la primera ecuacion: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuacion: "))
c = float(input("Ingrese la constante en la primera ecuación: "))

d = float(input("Ingrese el coeficiente de x en la segunda ecuacion: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuacion: "))
f = float(input("Ingrese la constante en la segunda ecuacion: "))

x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

x_redondeado = round(x, 1)
y_redondeado = round(y, 1)

print("x =", x_redondeado,",""y =",y_redondeado)  