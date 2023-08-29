#Sistema de Ecuaciones
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese la constante c1: "))

a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese la constante c2: "))

x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)

print("x =", x)
print("y =", y)
      