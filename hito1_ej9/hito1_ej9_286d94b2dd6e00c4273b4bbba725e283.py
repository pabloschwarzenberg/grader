def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        print("Las soluciones del sistema son:")
        print("x =", round(x, 1))
        print("y =", round(y, 1))

# Solicitar los valores del sistema al usuario
print("Ingrese los coeficientes del sistema de ecuaciones:")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))

# Resolver el sistema y mostrar las soluciones
resolver_sistema(a1, b1, c1, a2, b2, c2)
