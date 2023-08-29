#Sistema de Ecuaciones
a = float(input("Ingresa el valor de a -> "))        
b = float(input("Ingresa el valor de b -> "))
c = float(input("Ingresa el valor de c -> "))
d = float(input("Ingresa el valor de d -> "))
e = float(input("Ingresa el valor de e -> "))
f = float(input("Ingresa el valor de f -> "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print("X=",(x),"Y=",(y))      