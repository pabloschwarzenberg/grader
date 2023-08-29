#Sistema de Ecuaciones
def solve_equations(a, b, c, d, e, f):
    determinant = a * d - b * c
    if determinant == 0:
      return "El sistema no tiene solución única."
 x = (e * d - b * f) / determinant
 y = (a * f - c * e) / determinant
    return f"x = {round(x, 1)}\ny = {round(y, 1)}"
a = 2
b = 3
c = 1
d = 2
e = 6
f = 5

solution = solve_equations(a, b, c, d, e, f)
print(solution)     