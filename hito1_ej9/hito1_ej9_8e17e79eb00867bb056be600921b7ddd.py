def solve_equation_system(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
        print("El sistema no tiene solución única.")
    else:
        x = (e * d - b * f) / determinant
        y = (a * f - c * e) / determinant
        print(f"x={round(x, 1)}")
        print(f"y={round(y, 1)}")

# Ejemplo de uso: sistema 2x+3y=0 y x+2y=1
a = 2
b = 3
c = 0
d = 1
e = 2
f = 1

solve_equation_system(a, b, c, d, e, f)
