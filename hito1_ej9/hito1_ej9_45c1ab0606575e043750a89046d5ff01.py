def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1

    if determinante == 0:
        # El sistema no tiene solución única
        return None

    x = (b2 * c1 - b1 * c2) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    r = [x, y]
    return r

# Obtener los coeficientes del sistema del usuario
a1 = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b1 = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c1 = float(input("Ingrese el término independiente de la primera ecuación: "))
a2 = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
b2 = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
c2 = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Resolver el sistema
soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

# Mostrar las soluciones redondeadas a un decimal
if soluciones is None:
    print("El sistema no tiene solución única.")
else:
    print("x=", soluciones[0])
    print("y=", soluciones[1])
    
