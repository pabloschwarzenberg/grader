#Sistema de Ecuaciones
a = float(input('Ingrese valor a: '))
b = float(input('Ingrese valor b: '))
c = float(input('Ingrese valor c: '))
d = float(input('Ingrese valor d: '))
e = float(input('Ingrese valor e: '))
f = float(input('Ingrese valor f: '))

det = a * e - b * d

if det != 0:
    x = (c * e - b * f) / det
    y = (a * f - c * d) / det
    print('x=', x, ', y=', y)
       