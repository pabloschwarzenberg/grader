#Sistema de Ecuaciones
from math import *

a = float(input("Ingrese 1er numero: "))
b = float(input("Ingrese 2o numero: "))
c = float(input("Ingrese 3er numero: "))
d = float(input("Ingrese 4to numero: "))
e = float(input("Ingrese 5to numero: "))
f = float(input("Ingrese 6to numero: "))

solX = (f - (e*c/b)) / (d - (a*e/b))
solY = (f - (d*c/a)) / (e - (b*d/a))

x = round(solX, 1)
y = round(solY, 1)

print("x="+str(x))
print("y="+str(y))