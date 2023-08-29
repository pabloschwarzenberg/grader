# Obtener los valores del sistema de ecuaciones
a, b, c, d, e, f = map(float, input("Ingrese los valores del sistema de ecuaciones (a b c d e f): ").split())

# Calcular las soluciones del sistema de ecuaciones
determinante = a * e - b * d

if determinante != 0:
    x = round((c * e - b * f) / determinante, 1)
    y = round((a * f - c * d) / determinante, 1)
    print(f"x = {x}")
    print(f"y = {y}")
else:
    print("El sistema no tiene solución única.")