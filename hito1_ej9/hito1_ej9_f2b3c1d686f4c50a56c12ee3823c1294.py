#Sistema de Ecuaciones
def sistema_ecuaciones (A, B, C, a, b, c):
    discriminante = (A * b) - (a * B)

    if discriminante == 0:
        return "No tiene solución"
    else:
        x = ((C * b) - (c * B)) / discriminante
        y = ((A * c) - (a * C)) / discriminante
    x1 = str(round(x, 1))
    y1 = str(round(y, 1))
    print(['x =' + x1, 'y =' + y1])

A = int(input('Ingresa el valor de A: '))
B = int(input('Ingresa el valor de B: '))
C = int(input('Ingresa el valor de C: '))
a = int(input('Ingresa el valor de a: '))
b = int(input('Ingresa el valor de b: '))
c = int(input('Ingresa el valor de c: '))
sistema_ecuaciones (A, B, C, a, b, c)
