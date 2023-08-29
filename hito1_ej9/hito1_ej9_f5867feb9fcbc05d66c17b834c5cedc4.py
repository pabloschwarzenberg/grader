#Sistema de Ecuaciones
a = float(input("Ingrese numero A:"))
b = float(input("Ingrese numero B:"))
c = float(input("Ingrese numero C:"))
d = float(input("Ingrese numero D:"))
e = float(input("Ingrese numero E:"))
f = float(input("Ingrese numero F:"))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))