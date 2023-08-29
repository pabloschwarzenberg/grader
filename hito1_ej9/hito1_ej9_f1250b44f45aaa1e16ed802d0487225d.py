a = float(input("ingresa x1"))
b = float(input("ingresa y1"))
c = float(input("ingresa z1"))
d = float(input("ingresa x2"))
e = float(input("ingresa y2"))
f = float(input("ingresa z2"))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print('x='+str(x))
    print('y='+str(y))

else :
    m = d / a

    if m * c == f :
        print("El sistema tiene infinitas soluciones")
    else:
        print("El sistema no tiene soluciones")
