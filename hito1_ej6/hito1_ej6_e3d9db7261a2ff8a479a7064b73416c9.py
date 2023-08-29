#Ordenar tres números

x = int(input('Escribe el primer número: ' ))
y = int(input('Escribe el segundo número: '))
z = int(input('Escribe el tercer número: '))

a = min(x, y, z)
c = max(x, y, z)
b = (x +  y + z) - a - c 

# 1, 2, 3
# a = 1
# c = 3
# b = (1 + 2 + 3) - 1 - 3
# b = 6 - 1 - 3 = 2 

print('Los números ordenados son: {}, {} , {} '.format(a, b, c))