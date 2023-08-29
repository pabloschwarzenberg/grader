# Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Aplicar el método de eliminación de Gauss-Jordan
    det = a1 * b2 - a2 * b1
    if det == 0:
        # El sistema no tiene solución única
        return None

    # Calcular las soluciones
    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det

    return x, y


# Pedir los coeficientes del sistema al usuario
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Resolver el sistema
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Imprimir las soluciones redondeadas a un decimal
if soluciones is not None:
    x, y = soluciones
    print(f"x = {round(x, 1)}")
    print(f"y = {round(y, 1)}")
else:
    print("El sistema no tiene solución única.")
