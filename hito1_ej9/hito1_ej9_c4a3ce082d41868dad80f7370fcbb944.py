def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

if soluciones is None:
    print("El sistema no tiene solución única")
else:
    x, y = soluciones
    print(f"x = {x:.1f}")
    print(f"y = {y:.1f}")
