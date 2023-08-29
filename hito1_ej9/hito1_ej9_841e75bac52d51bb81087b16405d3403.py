#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):

    det = a1 * b2 - a2 * b1
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1
    

    if det != 0:

        x = det_x / det
        y = det_y / det
        return x, y
    elif det_x == 0 and det_y == 0:
        return "El sistema tiene infinitas soluciones."
    else:
        return "El sistema no tiene solución."

a1 = float(input("Ingrese el valor de a1: "))
b1 = float(input("Ingrese el valor de b1: "))
c1 = float(input("Ingrese el valor de c1: "))
a2 = float(input("Ingrese el valor de a2: "))
b2 = float(input("Ingrese el valor de b2: "))
c2 = float(input("Ingrese el valor de c2: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

if isinstance(soluciones, tuple):
    x = round(soluciones[0], 1)
    y = round(soluciones[1], 1)
    print("Las soluciones del sistema son:")
    print("x =", x)
    print("y =", y)
else:
    print(soluciones)