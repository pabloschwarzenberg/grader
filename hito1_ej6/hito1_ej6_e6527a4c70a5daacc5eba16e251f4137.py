#Ordenar tres números

x = int(input("Escriba el primer numero: "))
y = int(input("Escriba el segundo  numero: "))
z = int(input("Escriba el tercer numero numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z ) - a - c

# 9, 3, 6
# a = 9
# c = 6
# b = (9 + 3 + 6) - 9 - 6
# b = 18 - 9 - 6 = 6

print("Los numeros Ordenados son: {}, {}, {}.".format(a, b, c))      