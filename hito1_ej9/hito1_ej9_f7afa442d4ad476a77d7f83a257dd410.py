#Sistema de Ecuaciones
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))
determinante = a*e - b*d
x = (c*e - b*f) // determinante
y = (a*f - c*d) // determinante

print("x = " + str(x) + "y = " + str(y))