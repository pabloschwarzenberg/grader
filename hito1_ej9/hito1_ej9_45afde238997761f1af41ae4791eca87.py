def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    
    if determinante == 0:
        # El sistema no tiene solución única
        return None
    
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    
    return x, y

# Solicitar los valores del sistema al usuario
a1 = float(input("Ingrese el valor de a1: "))
b1 = float(input("Ingrese el valor de b1: "))
c1 = float(input("Ingrese el valor de c1: "))
a2 = float(input("Ingrese el valor de a2: "))
b2 = float(input("Ingrese el valor de b2: "))
c2 = float(input("Ingrese el valor de c2: "))

solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

if solucion:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única")

