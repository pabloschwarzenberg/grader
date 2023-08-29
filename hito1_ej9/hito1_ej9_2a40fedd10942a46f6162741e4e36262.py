def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    
    if determinante == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (e * d - b * f) / determinante
        y = (a * f - c * e) / determinante
        print("x=" + str(round(x, 1)))
        print("y=" + str(round(y, 1)))

# Ejemplo de uso
resolver_sistema(2, 3, 17, 1, 2, 9)