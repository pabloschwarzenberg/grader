def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        # El sistema no tiene solución única
        print("El sistema no tiene solución única")
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        print(f"x = {round(x, 1)}")
        print(f"y = {round(y, 1)}")
        