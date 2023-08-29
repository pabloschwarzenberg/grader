#Ordenar tres números
X = int(input("Ingrese el primer número: "))
Y = int(input("Ingrese el segundo número: "))
Z = int(input("Ingrese el tercer número: "))
a = min(X, Y, Z)
c = max(X, Y, Z)
b = (X + Y + Z) - a - c
# 1, 2, 3
# a = 1
# c = 3
# b = (1+ 2+ 3) - 1 - 3
# b = 6 - 1 - 3 = 2
print("Los números ordenados son: {}, {} , {}".format(a, b, c))