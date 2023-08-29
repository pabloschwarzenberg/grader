#Sistema de Ecuaciones
a = float(input("Ingrese un número :"))
b = float(input("Ingrese un segundo número:"))
c = float(input("Ingrese un tercer número:"))
d = float(input("Ingrese un cuarto número:"))
e = float(input("Ingrese un quinto número:"))
f = float(input("Ingrese sexto número:"))


x = (c * e - b * f) // (a * e - b * d)
y = (a * f - c * d) // (a * e - b * d)

print("x=" +str(x) + "y="+str(y))      