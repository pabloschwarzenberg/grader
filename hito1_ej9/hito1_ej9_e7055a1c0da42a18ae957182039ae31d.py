#Sistema de Ecuaciones
   def solve_equation(a, b, c, d, e, f):
    # Calcula el determinante
    determinant = a * d - b * c

    if determinant == 0:
        # El sistema no tiene solución única
        print("El sistema no tiene solución única.")
        return

    # Calcula las soluciones
    x = (e * d - b * f) / determinant
    y = (a * f - c * e) / determinant

    # Imprime las soluciones redondeadas a un decimal
    print("x = {:.1f}".format(x))
    print("y = {:.1f}".format(y))

# Ejemplo de uso
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

solve_equation(a, b, c, d, e, f)
   