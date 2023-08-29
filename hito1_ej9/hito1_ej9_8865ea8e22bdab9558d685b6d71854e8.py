#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        # El sistema no tiene solución única
        return None

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return round(x, 1), round(y, 1)

# Ejemplo de uso
soluciones = resolver_sistema(2, 3, 6, 1, 2, 5)
if soluciones is not None:
    x, y = soluciones
    print("x =", x)
    print("y =", y)
else:
    print("El sistema no tiene solución única")
     