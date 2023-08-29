#Sistema de Ecuaciones

def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return "El sistema no tiene solución única"

    x = round(((b2 * c1 - b1 * c2) / determinante), 1)
    y = round(((a1 * c2 - a2 * c1) / determinante), 1)

    return f"x={x}\ny={y}"


# Pedir al usuario los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Imprimir las soluciones del sistema
print(soluciones)