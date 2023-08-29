#Sistema de Ecuaciones
from sys import argv
script, a, b, c, d, e, f = argv

a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)
f = float(f)

det = a * e - b * d

if det != 0 :
    x = (e * c - b * f) / det
    y = (a * f - d * c) / det

    print "La solucion al sistema es x= %d e y= %d" % (x, y)

else :
    m = d / a

    if m * c == f :
        print "El sistema tiene infinitas soluciones"
    else:
        print "El sistema no tiene soluciones"