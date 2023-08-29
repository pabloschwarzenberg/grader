#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    # Calcular determinante
    det = a * d - b * c

    if det == 0:
        # El sistema no tiene solución única
        return None

    # Calcular soluciones
    x = (e * d - b * f) / det
    y = (a * f - c * e) / det

    return x, y


if __name__ == "__main__":
    # Leer los coeficientes del sistema
    a, b, c, d, e, f = map(float, input("Ingrese los coeficientes del sistema separados por espacios: ").split())

    # Resolver el sistema
    soluciones = resolver_sistema(a, b, c, d, e, f)

    if soluciones is None:
        print("El sistema no tiene solución única.")
    else:
        x, y = soluciones
        print("x =", round(x, 1))
        print("y =", round(y, 1))
