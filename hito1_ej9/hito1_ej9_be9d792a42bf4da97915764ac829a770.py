#Sistema de Ecuaciones
print("Ingrese los 6 numeros: ")
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())

det = (a * e) - (b * d)
if det!=0:
	x = ((c * e) - (b * f))/det
	y = ((a * f) - (c * d))/det
	print("x=",x)
	print("y=",y)
else:
	print("Notiene solucion")      