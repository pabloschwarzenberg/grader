#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calculamos el determinante de la matriz principal
    determinante = a1 * b2 - a2 * b1
    
    # Verificamos si el sistema tiene solución única
    if determinante == 0:
        print("El sistema no tiene solución única.")
        return
    
    # Calculamos las soluciones utilizando el método de eliminación
    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    
    # Imprimimos las soluciones redondeadas a un decimal
    print("x =", round(x, 1))
    print("y =", round(y, 1))

# Ejemplo de uso
a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

resolver_sistema(a1, b1, c1, a2, b2, c2)
