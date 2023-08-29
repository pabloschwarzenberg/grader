def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None

    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return ['x={}'.format(round(x, 1)), 'y={}'.format(round(y, 1))]


a1 = int(input("Ingrese el valor de a1: "))
b1 = int(input("Ingrese el valor de b1: "))
c1 = int(input("Ingrese el valor de c1: "))
a2 = int(input("Ingrese el valor de a2: "))
b2 = int(input("Ingrese el valor de b2: "))
c2 = int(input("Ingrese el valor de c2: "))

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

if solucion is None:
    print("El sistema no tiene solución única.")
else:
    for variable in solucion:
        print(variable)
