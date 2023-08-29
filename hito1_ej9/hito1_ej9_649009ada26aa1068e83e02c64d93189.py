def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c

    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y


# Ejemplo de uso
a = 2
b = 3
c = -23
d = 1
e = 2
f = -12

soluciones = resolver_sistema(a, b, c, d, e, f)
if soluciones is not None:
    x, y = soluciones
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")

