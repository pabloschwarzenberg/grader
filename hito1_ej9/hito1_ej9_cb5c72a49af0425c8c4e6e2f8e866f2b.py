#Sistema de Ecuaciones
# ax + by = c
# dx + ey = f

def soluciones_sistemas_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante

        return x, y
    else:
        return None, None

print('digite los valores a, b, c, d, e, f: ')
a, b, c, d, e, f = map(float, input().split())

print(soluciones_sistemas_ecuaciones(a, b, c, d, e, f))