#Sistema de Ecuaciones
a = float(input("Ingrese número para A:"))
b = float(input("Ingrese número para B:"))
c = float(input("Ingrese número para C:"))
d = float(input("Ingrese número para D:"))
e = float(input("Ingrese número para E:"))
f = float(input("Ingrese número para F:"))

x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("solución para x=" +str(x) + "solución para y="+str(y))