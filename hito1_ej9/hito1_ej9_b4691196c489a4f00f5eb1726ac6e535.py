# Leer los coeficientes del sistema de ecuaciones
a1, b1, c1 = map(float, input("Ingrese los coeficientes de la primera ecuación separados por espacios: ").split())
a2, b2, c2 = map(float, input("Ingrese los coeficientes de la segunda ecuación separados por espacios: ").split())

# Calcular las soluciones del sistema de ecuaciones
det = a1*b2 - a2*b1
if det != 0:
    x = (c1*b2 - c2*b1) / det
    y = (a1*c2 - a2*c1) / det
    print("Las soluciones son: x = {:.1f}, y = {:.1f}".format(x, y))
else:
    print("El sistema no tiene solución única.")
