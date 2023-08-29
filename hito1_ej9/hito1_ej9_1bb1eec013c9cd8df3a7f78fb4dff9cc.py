#Sistema de Ecuaciones
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
d = float(input("Ingrese el valor de d: "))
e = float(input("Ingrese el valor de e: "))
f = float(input("Ingrese el valor de f: "))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print ("x= ", round(x, 1))
    print("y= ", round(y, 1))

else :
    m = d / a

    if m * c == f :
        print ("El sistema tiene infinitas soluciones")
    else:
        print ("El sistema no tiene soluciones")     