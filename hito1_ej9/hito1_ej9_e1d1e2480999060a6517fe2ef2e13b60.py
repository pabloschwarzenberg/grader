a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el término independiente c1: "))

a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el término independiente c2: "))


detA = a1 * b2 - a2 * b1
detX = c1 * b2 - c2 * b1
detY = a1 * c2 - a2 * c1

if detA == 0:
    print("El sistema de ecuaciones no tiene solución única.")
else:
    x = detX / detA
    y = detY / detA

    x = round(x, 1)
    y = round(y, 1)

    print("La solución del sistema es:")
    print("x =", x)
    print("y =", y)