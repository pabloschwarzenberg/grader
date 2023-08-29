#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d

    if determinante == 0:
        print("El sistema no tiene solución")
    else:
        x = (c * e - b * f) / determinante
        y = (a * f - c * d) / determinante
        print("x =", round(x, 1))
        print("y =", round(y, 1))


# Ejemplo de uso
a = 2
b = 3
c = 6
d = 1
e = 2
f = 5

resolver_sistema(a, b, c, d, e, f)
