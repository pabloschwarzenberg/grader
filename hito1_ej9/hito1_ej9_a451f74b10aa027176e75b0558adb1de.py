#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Calcula el valor de y
    y = (c2*a1 - c1*a2) / (b2*a1 - b1*a2)
    # Calcula el valor de x
    x = (c1 - b1*y) / a1
    # Devuelve las soluciones redondeadas a un decimal
    return round(x, 1), round(y, 1)

# Solicita al usuario los coeficientes del sistema de ecuaciones
a1 = float(input("Ingrese el coeficiente a1: "))
b1 = float(input("Ingrese el coeficiente b1: "))
c1 = float(input("Ingrese el coeficiente c1: "))
a2 = float(input("Ingrese el coeficiente a2: "))
b2 = float(input("Ingrese el coeficiente b2: "))
c2 = float(input("Ingrese el coeficiente c2: "))

# Resuelve el sistema y muestra las soluciones
x, y = resolver_sistema(a1, b1, c1, a2, b2, c2)
print("x =", x)
print("y =", y)
