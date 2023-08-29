#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calculamos el determinante de la matriz de coeficientes
    determinante = a1 * b2 - a2 * b1

    # Verificamos si el sistema es compatible determinado (determinante diferente de cero)
    if determinante != 0:
        # Calculamos las soluciones para x e y
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        # Imprimimos las soluciones redondeadas a un decimal
        print("x =", round(x, 1))
        print("y =", round(y, 1))
    else:
        # El sistema no tiene solución única
        print("El sistema no tiene solución única.")

# Pedimos al usuario que ingrese los coeficientes del sistema
a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

# Llamamos a la función para resolver el sistema de ecuaciones
resolver_sistema(a1, b1, c1, a2, b2, c2)
