#Sistema de Ecuaciones
from sys import argv

a = float(input("Digite valor de a: "))        
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))
d = float(input("Digite valor de d: "))
e = float(input("Digite valor de e: "))
f = float(input("Digite valor de f: "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print("X=",(x),"Y=",(y))
      