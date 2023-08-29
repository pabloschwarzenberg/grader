def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calcular el determinante principal
    det_principal = a1 * b2 - a2 * b1
    if det_principal == 0:
        print('El sistema no tiene una única solución')
        return
    # Calcular los determinantes para x e y y resolver
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1
    x = det_x / det_principal
    y = det_y / det_principal
    # Crear las cadenas con los resultados redondeados
    res_x = 'x=' + str(round(x, 1))
    res_y = 'y=' + str(round(y, 1))
    print([res_x, res_y])

# Prueba del sistema de ejemplo
resolver_sistema(2, 3, 15, 1, 2, 12)

