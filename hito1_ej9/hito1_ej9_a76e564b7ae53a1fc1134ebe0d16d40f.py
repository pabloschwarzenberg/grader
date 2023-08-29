#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):

    determinante = a1 * b2 - a2 * b1

    determinante_x = c1 * b2 - c2 * b1

    determinante_y = a1 * c2 - a2 * c1

 

    if determinante == 0:

        return "El sistema no tiene solución única"

 

    x = round(determinante_x / determinante, 1)

    y = round(determinante_y / determinante, 1)

 

    return "x={:.1f}\ny={:.1f}".format(x, y)

 

# Solicitar los coeficientes del sistema al usuario

a1 = float(input("Ingresar coeficiente a1: "))

b1 = float(input("Ingresar coeficiente b1: "))

c1 = float(input("Ingresar coeficiente c1: "))

a2 = float(input("Ingresar coeficiente a2: "))

b2 = float(input("Ingresar coeficiente b2: "))

c2 = float(input("Ingresar coeficiente c2: "))

 

# Resolver el sistema y mostrar las soluciones

soluciones = resolver_sistema(a1, b1, c1, a2, b2, c2)

print(soluciones)