#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    if determinante == 0:
        # El sistema no tiene solución única
        return None
    else:
        x = (e * d - b * f) / determinante
        y = (a * f - c * e) / determinante
        return x, y

# Ejemplo de entrada
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

soluciones = resolver_sistema(a, b, c, d, e, f)

if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    # Imprimir las soluciones redondeadas a un decimal
    print(f'x = {soluciones[0]:.1f}')
    print(f'y = {soluciones[1]:.1f}')
