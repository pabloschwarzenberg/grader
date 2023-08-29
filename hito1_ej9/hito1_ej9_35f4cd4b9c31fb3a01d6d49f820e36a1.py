#Sistema de Ecuaciones
a = float(input("intoduce un Numero para A:"))
b = float(input("introduce un Numero para B:"))
c = float(input("introduce un Numero para C:"))
d = float(input("introduce un Numero para D:"))
e = float(input("introduce un Numero para E:"))
f = float(input("introduce un Numero para F:"))

x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)
print("x=" +str(x) + "y="+str(y))
