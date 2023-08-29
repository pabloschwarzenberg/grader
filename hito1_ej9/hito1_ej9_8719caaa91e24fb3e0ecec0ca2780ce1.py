#Sistema de Ecuaciones
a = float(input("valor de a: "))        
b = float(input("valor de b: "))
c = float(input("valor de c: "))
d = float(input("valor de d: "))
e = float(input("valor de e: "))
f = float(input("valor de f: "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print("X=",(x),"Y=",(y))     