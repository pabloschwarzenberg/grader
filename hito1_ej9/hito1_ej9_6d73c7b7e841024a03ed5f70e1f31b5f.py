#Sistema de Ecuaciones
a = float(input("Ingrese Numero para x:"))

b = float(input("Ingrese Numero para x1:"))

c = float(input("Ingrese Numero para x2:"))

d = float(input("Ingrese Numero para x3:"))

e = float(input("Ingrese Numero para x4:"))

f = float(input("Ingrese Numero para x5:"))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))