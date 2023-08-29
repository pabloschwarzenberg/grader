#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        return None  # El sistema no tiene solución única

    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return round(x, 1), round(y, 1)


# Solicitar los coeficientes del sistema al usuario
a1 = float(input("Ingrese valor a1: "))
b1 = float(input("Ingrese valor b1: "))
c1 = float(input("Ingrese valor c1: "))
a2 = float(input("Ingrese valor a2: "))
b2 = float(input("Ingrese valor b2: "))
c2 = float(input("Ingrese valor c2: "))

# Resolver el sistema
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Imprimir las soluciones
if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    print("Solución x:", soluciones[0])
    print("Solución y:", soluciones[1])
      