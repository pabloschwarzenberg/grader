#Sistema de Ecuaciones
a = float(input("Ingrese un numero"))
b = float(input("Ingrese otro numero:"))
c = float(input("Ingrese otro numero:"))
d = float(input("Ingrese otro numero:"))
e = float(input("Ingrese otro numero:"))
f = float(input("Ingrese otro numero:"))
x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)
print("x=" +str(x) + "y="+str(y))