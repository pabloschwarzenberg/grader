def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

# Ejemplo de uso del programa
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

if solucion is None:
    print("El sistema no tiene solución única.")
else:
    x, y = solucion
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")
