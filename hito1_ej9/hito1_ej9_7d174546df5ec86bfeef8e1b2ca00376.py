#Sistema de Ecuaciones
a = float(input("Ingrese Numero para A:"))
b = float(input("Ingrese Numero para B:"))
c = float(input("Ingrese Numero para C:"))
d = float(input("Ingrese Numero para D:"))
e = float(input("Ingrese Numero para E:"))
f = float(input("Ingrese Numero para F:"))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))