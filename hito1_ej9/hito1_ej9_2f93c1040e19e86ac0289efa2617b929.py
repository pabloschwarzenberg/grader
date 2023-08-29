#Sistema de Ecuaciones
def solucion_sistema_ecuaciones(a, b, c, d, e, f):
    determinante = ae - bd 


    if determinante != 0:
        y = (af - cd) / determinante
        x = (ce - bf) / determinante

        return x, y

    else:
        return None, None

print('digite los valores para a, b, c, d, e, f : ')
a, b, c, d, e, f = map(float, input().split())

print(solucion_sistema_ecuaciones)