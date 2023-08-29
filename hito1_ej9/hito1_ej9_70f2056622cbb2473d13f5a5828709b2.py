#Sistema de Ecuaciones
def solve_system(a1, b1, c1, a2, b2, c2):
    eq1 = (a1 * b2, b1 * b2, c1 * b2)
    eq2 = (a2 * b1, b2 * b1, c2 * b1)
    eq3 = (eq1[0] - eq2[0], eq1[1] - eq2[1], eq1[2] - eq2[2])
    x = eq3[2] / eq3[0]
    y = (c1 - a1 * x) / b1

    print("x =", round(x, 1))
    print("y =", round(y, 1))

#Ejemplo de uso
a1 = int(input(""))
b1 = int(input(""))
c1 = int(input(""))
a2 = int(input(""))
b2 = int(input(""))
c2 = int(input(""))

solve_system(a1, b1, c1, a2, b2, c2)