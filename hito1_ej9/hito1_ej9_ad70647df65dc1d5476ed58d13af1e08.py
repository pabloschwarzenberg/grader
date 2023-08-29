#Sistema de Ecuaciones

a = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c = float(input("Ingrese el término independiente 'c' de la primera ecuación: "))
d = float(input("Ingrese el coeficiente 'd' de la segunda ecuación: "))
e = float(input("Ingrese el coeficiente 'e' de la segunda ecuación: "))
f = float(input("Ingrese el término independiente 'f' de la segunda ecuación: "))


denominador = a * e - b * d
x = (c * e - b * f) / denominador
y = (a * f - c * d) / denominador


print("x =", round(x, 1))
print("y =", round(y, 1))

      