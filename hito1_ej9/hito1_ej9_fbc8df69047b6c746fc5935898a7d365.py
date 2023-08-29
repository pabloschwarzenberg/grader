#Sistema de Ecuaciones
# ax + by = c
# dx + ey = f
def solucion_sistema(a,b,c,d,e,f):
    determinante = a*e - b*d

    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante

        return x,y
    else:
        return None,None


print('Digite los valores para a, b, c, d, e, f: ')
a,b,c,d,e,f = map(float, input().split(0))

print(solucion_sistema(a,b,c,d,e,f))      