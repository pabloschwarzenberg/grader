#Sistema de Ecuaciones

def sistema_de_ecuaciones(a, b, c, d, e, f):
    det = a * e - b * d
    if det != 0:
        x = (c * e - b * f) / det
        y = (a * f - c * d) / det
        print('x=',x)
        print('y=',y)
        return x, y
    else:
        return None, None


print('Digite los valores del sistema de ecuaciones:')
a = int(input('ax = '))
b = int(input('by = '))
c = int(input('c = '))
d = int(input('dx = '))
e = int(input('ey = '))
f = int(input('f = '))

sistema_de_ecuaciones(a, b, c, d, e, f)
