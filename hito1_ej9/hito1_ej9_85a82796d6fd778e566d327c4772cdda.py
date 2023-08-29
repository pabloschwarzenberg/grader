#Sistema de Ecuaciones
# Función para resolver un sistema de dos ecuaciones con dos incógnitas
def resolver_sistema(a, b, c, d, e, f):
    # Calculamos determinante
    determinante = a * e - b * d
    
    # Verificamos si el sistema tiene solución
    if determinante == 0:
        return None  # No tiene solución
    
    # Calculamos las soluciones
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante
    
    return x, y

# Entrada de datos
a = float(input("Ingrese el coeficiente de x en la primera ecuación: "))
b = float(input("Ingrese el coeficiente de y en la primera ecuación: "))
c = float(input("Ingrese el resultado de la primera ecuación: "))
d = float(input("Ingrese el coeficiente de x en la segunda ecuación: "))
e = float(input("Ingrese el coeficiente de y en la segunda ecuación: "))
f = float(input("Ingrese el resultado de la segunda ecuación: "))

# Resolver el sistema
solucion = resolver_sistema(a, b, c, d, e, f)

# Imprimir soluciones redondeadas a un decimal
if solucion is None:
    print("El sistema no tiene solución.")
else:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
