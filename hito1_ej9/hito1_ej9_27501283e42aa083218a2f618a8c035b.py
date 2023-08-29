#Sistema de Ecuaciones
from sys import argv

z = float(input("Ingresa el valor de z: "))        
m = float(input("Ingresa el valor de m: "))
t = float(input("Ingresa el valor de t: "))
r = float(input("Ingresa el valor de r: "))
s = float(input("Ingresa el valor de s: "))
h = float(input("Ingresa el valor de h: "))

det = z * s - m * r

if det != 0 :
    x = (s * t - m * h) / det
    y = (z * h - r * t) / det

    print("X=",(x),"Y=",(y))      