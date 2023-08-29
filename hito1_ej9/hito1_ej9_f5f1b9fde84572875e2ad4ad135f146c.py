#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * e - b * d

    if determinante == 0:
        return "El sistema no tiene solución única."

    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante

    solucion_x = round(x, 1)
    solucion_y = round(y, 1)

    return f"x = {solucion_x}, y = {solucion_y}"

# Ejemplo de uso
sistema = resolver_sistema(2, 3, 6, 1, 2, 5)
print(sistema)