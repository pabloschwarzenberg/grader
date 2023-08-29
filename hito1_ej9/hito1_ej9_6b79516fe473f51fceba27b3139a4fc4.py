#sistema de ecuaciones
def sis_ecuaciones(a, b, c, d, e, f):
    determinante= a*e - b*d
    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante
        return x, y
    else:
        return None, None
    

valores = len(input("Valores a, b, c, d , e y f: "))
a, b, c, d, e, f = map(float, int(valores.split()))

print(sis_ecuaciones(a, b, c, d, e,f))
