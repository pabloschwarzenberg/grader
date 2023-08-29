#Sistema de Ecuaciones
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = float(input('d: '))
e = float(input('e: '))
f = float(input('f: '))

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print ("La solucion al sistema es x= %.1f d  y= %.1f d" % (x, y))

else :
    m = d / a

    if m * c == f :
        print ("El sistema tiene infinitas soluciones")
    else:
        print ("El sistema no tiene soluciones")
