#Sistema de Ecuaciones
# Resolver sistema de ecuaciones

eq1 = [0, 0, 0]
eq2 = [0, 0, 0]

#Valores ecuacion 1
eq1[0] = int(input("Ingrese el valor de a: "))
eq1[1] = int(input("Ingrese el valor de b: "))
eq1[2] = int(input("Ingrese el valor de c: "))

#Valores ecuacion 2
eq2[0] = int(input("Ingrese el valor de d: "))
eq2[1] = int(input("Ingrese el valor de e: "))
eq2[2] = int(input("Ingrese el valor de f: "))

if eq1[0] > 0 and eq2[0] > 0 or eq1[0] < 0 and eq2[0] < 0 or eq1[0] == eq2[0]:
    a = eq1[0]
    eq1[0] = eq1[0] * -eq2[0]
    eq1[1] = eq1[1] * -eq2[0]
    eq1[2] = eq1[2] * -eq2[0]
    eq2[0] = eq2[0] * a
    eq2[1] = eq2[1] * a
    eq2[2] = eq2[2] * a
else:
    a = eq1[0]
    eq1[0] *= eq2[0]
    eq1[1] *= eq2[0]
    eq1[2] *= eq2[0]
    eq2[0] *= a
    eq2[1] *= a
    eq2[2] *= a

y = round((eq1[2] + eq2[2]) / (eq1[1] + eq2[1]), 1)
x = round(eq1[2] - (eq1[1] * y)) / eq1[0]

if x == -0:
    x = 0
elif y == -0:
    y = 0

print("x={0}".format(x))
print("y={0}".format(y))
