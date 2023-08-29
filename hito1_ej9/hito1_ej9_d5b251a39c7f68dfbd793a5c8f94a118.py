#Sistema de Ecuaciones
def resolver_sistema(a, b, c, d, e, f):
    determinante = a * d - b * c
    
    if determinante == 0:
        # El sistema no tiene solución única
        return None
    
    x = (e * d - b * f) / determinante
    y = (a * f - c * e) / determinante
    
    return round(x, 1), round(y, 1)

# Obtener los valores del sistema de ecuaciones
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el término independiente de la primera ecuación: "))

d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el término independiente de la segunda ecuación: "))

# Resolver el sistema de ecuaciones
soluciones = resolver_sistema(a, b, c, d, e, f)

if soluciones is not None:
    x, y = soluciones
    print("La solución del sistema es:")
    print("x =", x)
    print("y =", y)
else:
    print("El sistema no tiene solución única.")