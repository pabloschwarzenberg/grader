def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c

    if determinante == 0:
        return None  # No se puede resolver el sistema

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y

# Ejemplo de uso
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

solucion = resolver_sistema(a, b, c, d, e, f)

if solucion is None:
    print("No se puede resolver el sistema.")
else:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
