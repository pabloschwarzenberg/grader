def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return "El sistema no tiene solución única."
    else:
        x = (b2 * c1 - b1 * c2) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
     return f"x = {round(x, 1)}\ny = {round(y, 1)}"


# Ejemplo de uso
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)
print(soluciones)