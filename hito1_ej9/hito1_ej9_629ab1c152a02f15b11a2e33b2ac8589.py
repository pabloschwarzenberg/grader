#Sistema de Ecuaciones
def ecuaciones(a, b, c, d, e, f):
    calculo = a*e - b*d

    if calculo != 0:
        x = (c*e - b*f) / calculo
        y = (a*f - c*d) / calculo

        return x, y

    else:
         return None, None
print('Ingresa los numeros para a, b, c, d, e y f: ')
a, b, c, d, e, f = map(float, input().split())
print(ecuaciones(a, b, c, d, e, f))      