#Sistema de Ecuaciones
a = int(input("Ingrese numero: "))
b = int(input("Ingrese numero: "))
c = int(input("Ingrese numero: "))
d = int(input("Ingrese numero: "))
e = int(input("Ingrese numero: "))
f = int(input("Ingrese numero: "))
determinante = a * e - b * d
if determinante != 0:
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante
    print("x=" + str(x))
    print("y=" + str(y))
else:
    print("Error")
