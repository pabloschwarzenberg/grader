def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print(“El sistema no tiene solución única.”)
        return

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    print(“x =“, round(x, 1))
    print(“y =“, round(y, 1))

a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

resolver_sistema(a1, b1, c1, a2, b2, c2)