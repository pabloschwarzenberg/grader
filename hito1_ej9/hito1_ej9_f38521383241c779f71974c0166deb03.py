#Sistema de Ecuaciones
a = float(input("Ingrese un numero para a:"))
b = float(input("Ingrese un numero para b:"))
c = float(input("Ingrese un numero para c:"))
d = float(input("Ingrese un numero para d:"))
e = float(input("Ingrese un numero para e:"))
f = float(input("Ingrese un numero para f:"))

determinante = a*e-b*d

x = (c*e - b*f) / determinante
y = (a*f - c*d) / determinante

print("x=" + str(x) + "y=" + str(y))
