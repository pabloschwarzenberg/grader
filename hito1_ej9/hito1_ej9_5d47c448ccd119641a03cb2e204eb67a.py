#sistema de ecuaciones
q = float(input("Ingrese Numero para Q:"))
w = float(input("Ingrese Numero para W:"))
e = float(input("Ingrese Numero para E:"))
r = float(input("Ingrese Numero para R:"))
f = float(input("Ingrese Numero para F:"))
z = float(input("Ingrese Numero para Z:"))


x = (e * f - w * z) // (q * f - w * r)
y = (q * z - e * r) // (q * f - w * r)

print("x=" +str(x) + "y="+str(y))
