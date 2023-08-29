#Ordenar tres números
x = int(input('escriba el primer número: '))
y = int(input('escriba el segundo número: '))
z = int(input('escriba el tercer número: '))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print('Los números ordenados de menor a mayor son: {}, {}, {}'.format(a, b, c))