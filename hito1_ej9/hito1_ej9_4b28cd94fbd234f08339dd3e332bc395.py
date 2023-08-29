ecuacion1 = input()
ecuacion2 = input()

ecuacion1 = ecuacion1.replace(' ', '')
ecuacion2 = ecuacion2.replace(' ', '')

a1, b1, c1 = map(float, ecuacion1.split('x')[0].split('+'))
a2, b2, c2 = map(float, ecuacion2.split('x')[0].split('+'))

denominador = a1 * b2 - a2 * b1

if denominador != 0:
    x = (b2 * c1 - b1 * c2) / denominador
    y = (a1 * c2 - a2 * c1) / denominador

    x = round(x, 1)
    y = round(y, 1)

    print('x =', x)
    print('y =', y)
else:
    print('El sistema de ecuaciones no tiene solucion.')
