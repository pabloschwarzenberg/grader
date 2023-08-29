#Sistema de Ecuaciones
numero=input(print('ingrese numeros: '))
def numero(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (e * d - b * f) / determinant
        y = (a * f - c * e) / determinant
        print("x =", round(x, 1))
        print("y =", round(y, 1))



 