#Sistema de Ecuaciones
def resolver_sistema_ecuaciones(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        print("El sistema de ecuaciones no tiene solución única.")
        return

    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante

    print("Soluciones del sistema:")
    print("x =", round(x, 1))  # Modifica esta línea con la solución deseada
    print("y =", round(y, 1))  # Modifica esta línea con la solución deseada

# Pedimos al usuario que ingrese los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente 'a' de la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente 'b' de la primera ecuación: "))
c1 = float(input("Ingrese el término independiente 'c' de la primera ecuación: "))

a2 = float(input("Ingrese el coeficiente 'a' de la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente 'b' de la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente 'c' de la segunda ecuación: "))

# Resolvemos el sistema de ecuaciones utilizando el método de eliminación de Gauss
resolver_sistema_ecuaciones(a1, b1, c1, a2, b2, c2)
