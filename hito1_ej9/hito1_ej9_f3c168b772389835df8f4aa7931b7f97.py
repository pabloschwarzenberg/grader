#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calcular determinante
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        # El sistema no tiene solución única
        print("El sistema no tiene solución única")
    else:
        # Calcular las soluciones
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        # Imprimir las soluciones redondeadas a un decimal
        print("x =", round(x, 1))
        print("y =", round(y, 1))

# Solicitar al usuario ingresar los coeficientes del sistema
a1 = float(input("Coeficiente a1: "))
b1 = float(input("Coeficiente b1: "))
c1 = float(input("Coeficiente c1: "))
a2 = float(input("Coeficiente a2: "))
b2 = float(input("Coeficiente b2: "))
c2 = float(input("Coeficiente c2: "))

# Resolver el sistema e imprimir las soluciones
resolver_sistema(a1, b1, c1, a2, b2, c2)
