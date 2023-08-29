x1=0
y1=0
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única.")
        return

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    x1=str(round(x, 1))
    y1=str(round(y, 1))

    return x1,y1
print((["x=" + str(round(x1, 1)),"y=" + str(round(y1, 1))]))
