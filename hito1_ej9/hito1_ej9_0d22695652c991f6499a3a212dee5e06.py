def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c

    if determinante == 0:
        return None  # No hay solución única

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y

# Ejemplo de uso:
a = 2
b = 3
c = 3
d = 1
e = 2
f = 3

solucion = resolver_sistema(a, b, c, d, e, f)

if solucion is None:
    print("El sistema no tiene una solución única.")
else:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
