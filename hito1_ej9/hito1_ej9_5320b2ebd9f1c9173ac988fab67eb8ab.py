#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Eliminación de la primera incógnita
    k = a2 / a1
    b2 = b2 - k * b1
    c2 = c2 - k * c1

    # Resolución de la segunda ecuación
    y = c2 / b2

    # Resolución de la primera ecuación
    x = (c1 - b1 * y) / a1

    print("x={}".format(round(x, 1)))
    print("y={}".format(round(y, 1)))

resolver_sistema(2, 3, -24, 1, 2, -13)
