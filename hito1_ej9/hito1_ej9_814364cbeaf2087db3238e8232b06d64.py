a = float(input("Introduce el coeficiente a: "))
b = float(input("Introduce el coeficiente b: "))
c = float(input("Introduce el coeficiente c: "))
d = float(input("Introduce el coeficiente d: "))
e = float(input("Introduce el coeficiente e: "))
f = float(input("Introduce el coeficiente f: "))

det = a * e - b * d

if det == 0:
    print("El sistema no tiene solucion unica")
else:
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det

    print("x=" + str(x))
    print("y=" + str(y))
