def resolverSistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None  # El sistema no tiene solución única
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        return (x, y)

a1 = float(input("Coeficiente a1: "))
b1 = float(input("Coeficiente b1: "))
c1 = float(input("Coeficiente c1: "))
a2 = float(input("Coeficiente a2: "))
b2 = float(input("Coeficiente b2: "))
c2 = float(input("Coeficiente c2: "))

solucion = resolverSistema(a1, b1, c1, a2, b2, c2)
if solucion is not None:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")
