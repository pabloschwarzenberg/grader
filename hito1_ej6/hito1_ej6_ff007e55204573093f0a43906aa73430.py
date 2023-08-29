#Ordenar tres números

x = int(input("Ingrese su primer numero: "))
y = int(input("Ingrese su segundo numero: "))
z = int(input("Ingrese su tercer numero: "))

a = min(x, y , z)
c = max(x, y, z)
b = (x + y + z) - a - c

# 1, 2, 3
# a = 1
# c = 2
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2

print("Los Numeros ordenados de menor a mayor son: {}, {}, {}".format(a, b, c))
