#Ordenar tres números

x = int(input('Escribir el primer número: '))
y = int(input('Escibir el segundo número: '))
z = int(input('Escribir el tercer número: '))

a = min((x <= y), z)
c = max(x, (y <= z))
b = (x <= y <= z)

# 1, 2, 3
# a = 1
# b = 2
# c = 3

print('Los números ordenados son: {}, {} y {}'.format(a, b, c))