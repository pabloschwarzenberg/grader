#Sistema de Ecuaciones
      def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calcula determinante
    determinante = a1 * b2 - a2 * b1

    # Verifica si el sistema es compatible determinado o indeterminado
    if determinante == 0:
        return None  # El sistema no tiene solución única

    # Calcula las soluciones
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    return x, y

if __name__ == "__main__":
    a1 = float(input("Ingrese el coeficiente de x de la primera ecuación: "))
    b1 = float(input("Ingrese el coeficiente de y de la primera ecuación: "))
    c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
    a2 = float(input("Ingrese el coeficiente de x de la segunda ecuación: "))
    b2 = float(input("Ingrese el coeficiente de y de la segunda ecuación: "))
    c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

    soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

    if soluciones is None:
        print("El sistema no tiene solución única.")
    else:
        x, y = soluciones
        print("x =", round(x, 1))
        print("y =", round(y, 1))