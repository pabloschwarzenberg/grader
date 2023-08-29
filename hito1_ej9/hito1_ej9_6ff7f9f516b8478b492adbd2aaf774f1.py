#Sistema de Ecuaciones
a11 = float(input("Ingrese el coeficiente a11: "))
a12 = float(input("Ingrese el coeficiente a12: "))
b1 = float(input("Ingrese el término independiente b1: "))
a21 = float(input("Ingrese el coeficiente a21: "))
a22 = float(input("Ingrese el coeficiente a22: "))
b2 = float(input("Ingrese el término independiente b2: "))
detA = a11 * a22 - a12 * a21
detX = b1 * a22 - b2 * a12
detY = a11 * b2 - a21 * b1
if detA != 0:
    x = detX / detA
    y = detY / detA
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única")      