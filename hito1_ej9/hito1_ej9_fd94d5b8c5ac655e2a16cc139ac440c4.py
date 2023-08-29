def resolver_sistema(a, b, c, d, e, f):
    # Calcular determinante
    determinante = a * d - b * c

    # Verificar si el sistema tiene solución única
    if determinante == 0:
        return None

    # Calcular las soluciones
    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    return x, y

# Ejemplo de uso
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

soluciones = resolver_sistema(a, b, c, d, e, f)

if soluciones is not None:
    x, y = soluciones
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
