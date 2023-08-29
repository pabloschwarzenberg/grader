#Sistema de Ecuaciones
def sistema_ecuaciones(a, b, c, d, e, f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (ce - bf)/determinante
        y = (af - cd)/determinante
        return x,y
    else:
        return None, None
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
X = (a, b, c, d, e, f)
determinante = a* e - b* d
if determinante != 0:
        x = (c* e - b* f) / determinante
        y = (a* f - c* d) / determinante
        print("[x = ", x, ", ", "y = ", y, "]")
