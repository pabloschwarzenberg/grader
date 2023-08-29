def solve_linear_system(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        print("El sistema no tiene solución única.")
        return

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return x, y

a1 = float(input("Ingrese el valor de a en la primera ecuación: "))
b1 = float(input("Ingrese el valor de b en la primera ecuación: "))
c1 = float(input("Ingrese el valor de c en la segunda ecuación: "))
a2 = float(input("Ingrese el valor de d en la segunda ecuación: "))
b2 = float(input("Ingrese el valor de e en la tercera ecuación: "))
c2 = float(input("Ingrese el valor de f en la tercera ecuación: "))

solucion = solve_linear_system(a1, b1, c1, a2, b2, c2)

r1 = round(solucion[0], 1)
r2 = round(solucion[1], 1)
print("x=",r1)
print("y=",r2)
