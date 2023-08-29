def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y

# Ejemplo de uso:
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

solucion = resolver_sistema(a, b, c, d, e, f)

if solucion is None:
    print("El sistema no tiene solución única.")
else:
    x, y = solucion
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")