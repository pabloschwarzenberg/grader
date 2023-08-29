def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y


# Ejemplo: 2x + 3y = 6, x + 2y = 5
a1, b1, c1 = 2, 3, 6
a2, b2, c2 = 1, 2, 5

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)
if solucion is not None:
    x, y = solucion
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")
else:
    print("El sistema no tiene solución única.")
