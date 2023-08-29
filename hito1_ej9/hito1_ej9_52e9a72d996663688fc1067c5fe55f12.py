#Sistema de Ecuaciones
def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    
    if determinante == 0:
        # El sistema no tiene solución única
        return None
    
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    
    return x, y
a1 = float(input("Ingrese variable x del primer sistema: "))
b1 = float(input("Ingrese variable y del primer sistema: "))
c1 = float(input("Ingrese resultado del primer sistema: "))
a2 = float(input("Ingrese variable x del segundo sistema: "))
b2 = float(input("Ingrese variable y del segundo sistema: "))
c2 = float(input("Ingrese resultado del segundo sistema: "))
solucion = resolver_sistema(a1, b1, c1, a2, b2, c2)

if solucion is not None:
    x, y = solucion
    print("x =", round(x, 1))
    print("y =", round(y, 1))
else:
    print("El sistema no tiene solución única.")