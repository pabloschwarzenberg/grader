a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese la constante c1: "))

a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese la constante c2: "))

denominador = a1 * b2 - a2 * b1

if denominador != 0:
    x = (b2 * c1 - b1 * c2) / denominador
    y = (a1 * c2 - a2 * c1) / denominador

    print("x =", x)
    print("y =", y)
else:
    print("El sistema de ecuaciones no tiene solución única.")
