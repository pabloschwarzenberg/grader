def Lol(a, b, c, d, e, f):
    der = a * e - b * d

    if der == 0:
        print('El sistema no tiene solucion unica.')
        return

    x = (c * e - b * f) / der
    y = (a * f - c * d) / der

    print('x ='+str(x))
    print('y ='+str(y))

a = float(input('ingrese un numero:'))
b = float(input('ingrese un numero:'))
c = float(input('ingrese un numero:'))
d = float(input('ingrese un numero:'))
e = float(input('ingrese un numero:'))
f = float(input('ingrese un numero:'))

Lol(a, b, c, d, e, f)