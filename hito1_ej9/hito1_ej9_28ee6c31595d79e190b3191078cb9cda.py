#Sistema de Ecuaciones
def solve_system(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1

    if det != 0:
        x1 = (c1 * b2 - c2 * b1) / det
        x2 = (a1 * c2 - a2 * c1) / det
        round(x1, 1)
        round(x2, 1)
        print('x=',x1,'y=',x2)
    else:
        print("El sistema de ecuaciones no tiene solución única.")

a1 = float(input("Ingrese el coeficiente 'a1': "))
b1 = float(input("Ingrese el coeficiente 'b1': "))
c1 = float(input("Ingrese el término independiente 'c1': "))
a2 = float(input("Ingrese el coeficiente 'a2': "))
b2 = float(input("Ingrese el coeficiente 'b2': "))
c2 = float(input("Ingrese el término independiente 'c2': "))

solve_system(a1, b1, c1, a2, b2, c2)      