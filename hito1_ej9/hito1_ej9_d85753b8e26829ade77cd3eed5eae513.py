#Sistema de Ecuaciones
 from this import d


def solucion_sistema_ecuaciones(a, b, c, e, f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante

        return x, y
    else:
        return None, None


print('Digite los valores para a, b, d, e, y f: ')
a, b, c, d, e, f = map(float, input().slpit())

print(solucion_sistema_ecuaciones(a, b, c, d, e, f))     