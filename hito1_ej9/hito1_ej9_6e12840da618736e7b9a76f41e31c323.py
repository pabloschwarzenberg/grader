def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c

    if determinante == 0:
        print("El sistema no tiene solución única.")
        return

    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante

    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")


# Ejemplo de uso
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

resolver_sistema(a, b, c, d, e, f)
