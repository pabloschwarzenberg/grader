#Sistema de ecuaciones
a = float(input("Ingrese un valor para a: "))
b = float(input("Ingrese un valor para b: "))
c = float(input("Ingrese un valor para c: "))
d = float(input("Ingrese un valor para d: "))
e = float(input("Ingrese un valor para e: "))
f = float(input("Ingrese un valor para f: "))

x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))