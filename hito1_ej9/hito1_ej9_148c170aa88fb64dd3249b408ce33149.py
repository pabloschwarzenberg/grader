#Sistema de Ecuaciones
a = float(input("Ingrese Ax:"))
b = float(input("Ingrese By:"))
c = float(input("Ingrese C:"))
d = float(input("Ingrese Dx:"))
e = float(input("Ingrese Ey:"))
f = float(input("Ingrese F:"))
x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)
print("x=" +str(x) + "y="+str(y))