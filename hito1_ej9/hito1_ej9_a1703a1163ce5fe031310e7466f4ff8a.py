#Sistema de Ecuaciones

a1 = float(input('Ingrese el coeficiente de x en la primera ecuación: '))
b1 = float(input('Ingrese el coeficiente de y en la primera ecuación: '))
c1 = float(input('Ingrese el lado derecho de la primera ecuación: '))

a2 = float(input('Ingrese el coeficiente de x en la segunda ecuación: '))
b2 = float(input('Ingrese el coeficiente de y en la segunda ecuación: '))
c2 = float(input('Ingrese el lado derecho de la segunda ecuación: '))


d = a1 * b2 - a2 * b1
x = (c1 * b2 - c2 * b1) / d
y = (a1 * c2 - a2 * c1) / d

x = round(x, 1)
y = round(y, 1)
print('x =', x)
print('y =', y)


     