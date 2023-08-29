#Sistema de Ecuaciones
a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

def solve_equation(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1

    if determinant == 0:
        print("El sistema no tiene solución única.")
        return

    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    solution = ['x=' + str(round(x, 1)), 'y=' + str(round(y, 1))]
    print(solution)

solve_equation(a1, b1, c1, a2, b2, c2)
