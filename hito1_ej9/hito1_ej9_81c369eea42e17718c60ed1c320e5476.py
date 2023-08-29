#Sistema de Ecuaciones
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
a2 = int(input("Ingrese el valor de a2: "))
b2 = int(input("Ingrese el valor de b2: "))
c2 = int(input("Ingrese el valor de c2: "))

det = (a * b2) - (b * a2)

if det != 0:
    x = round(((b2 * c) - (b * c2)) / det, 1)
    y = round(((a * c2) - (a2 * c)) / det, 1)
    print("x = {0}".format(x))
    print("y = {0}".format(y))
