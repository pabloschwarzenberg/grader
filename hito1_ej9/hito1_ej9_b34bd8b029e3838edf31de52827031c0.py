#Sistema de Ecuaciones
x1 = float(input("Ingrese el coeficiente   x1: "))
y1 = float(input("Ingrese el coeficiente   y1: "))
c1 = float(input("Ingrese la constante c1: "))

x2 = float(input("Ingrese el coeficiente a2: "))
y2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese la constante c2: "))

# Resolver el sistema de ecuaciones
denominador = x1 * y2 - x2 * y1

if denominador != 0:
    x = (y2 * c1 - y1 * c2) / denominador
    y = (x1 * c2 - x2 * c1) / denominador

    # Imprimir las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema de ecuaciones no tiene solución única.")      