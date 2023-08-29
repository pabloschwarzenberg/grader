#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return "El sistema no tiene solución única."
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        return x, y

# Solicitar los coeficientes del sistema al usuario
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

# Resolver el sistema y mostrar las soluciones
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

if isinstance(soluciones, str):
    print(soluciones)
else:
    x, y = soluciones
    print("Las soluciones son:")
    print("x =", round(x, 1))
    print("y =", round(y, 1))
 