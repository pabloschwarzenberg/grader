def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (b2 * c1 - b1 * c2) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        print("x =", round(x, 1))
        print("y =", round(y, 1))

# Ejemplo de uso
resolver_sistema(2, 3, 6, 1, 2, 5)
