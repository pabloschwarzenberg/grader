def solve_system(a1, b1, c1, a2, b2, c2):
    # calculamos el denominador
    denom = a1 * b2 - a2 * b1
    # si el denominador es cero, el sistema no tiene solución
    if denom == 0:
        return None
    # calculamos las soluciones
    x = (c1 * b2 - c2 * b1) / denom
    y = (a1 * c2 - a2 * c1) / denom
    # redondeamos las soluciones a un decimal
    x = round(x, 1)
    y = round(y, 1)
    # devolvemos las soluciones
    return x, y
