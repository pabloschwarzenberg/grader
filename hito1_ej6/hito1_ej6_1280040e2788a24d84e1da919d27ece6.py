#Juan Andrés Guzman
from math import floor
A=float(input("ingrese un numero entero"))
B=float(input("ingrese un segundo numero entero"))
C=float(input("ingrese un tercer numero entero"))

x=floor(min(A, B, C))
z=floor(max(A, B, C))
y=floor(A + B + C - x - z)
print(x,",",y,",",z)