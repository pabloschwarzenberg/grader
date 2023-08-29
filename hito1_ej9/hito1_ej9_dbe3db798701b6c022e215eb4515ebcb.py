#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calcular el valor de x
    x = (c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1)
    # Calcular el valor de y utilizando el valor de x
    y = (c1 - a1 * x) / b1
    # Crear una lista con las soluciones redondeadas a un decimal como cadenas
    soluciones = ['x={:.1f}'.format(x), 'y={:.1f}'.format(y)]
    # Devolver la lista de soluciones
    return soluciones
a1 = int(input("Coloca un numero: "))
b1 = int(input("Coloca un numero: "))
c1 = int(input("Coloca un numero: "))
a2 = int(input("Coloca un numero: "))
b2 = int(input("Coloca un numero: "))
c2 = int(input("Coloca un numero: "))
print(resolver_sistema(a1, b1, c1, a2, b2, c2))