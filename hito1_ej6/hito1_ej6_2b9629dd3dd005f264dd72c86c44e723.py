#Ordenar tres números

x = int(input("escriba el primer numero: "))
y = int(input("escriba el segundo numero: "))
z = int(input("escriba el tercer numero: "))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

# 1, 2, 3
# a = 1
# c = 3
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2

print("los numeros ordenados son: {}, {}, {}".format(a, b, c))