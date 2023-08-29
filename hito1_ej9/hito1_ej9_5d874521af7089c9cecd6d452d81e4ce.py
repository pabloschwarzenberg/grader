#Sistema de Ecuaciones
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el término independiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el término independiente c2: "))


determinante = a1 * b2 - a2 * b1
x = (b2 * c1 - b1 * c2) / determinante
y = (a1 * c2 - a2 * c1) / determinante


print("x =", round(x, 1))
print("y =", round(y, 1))      