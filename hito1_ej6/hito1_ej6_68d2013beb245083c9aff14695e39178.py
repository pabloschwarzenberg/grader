#Ordenar tres números
a = int(input('Ingrese el primer número:'))
b = int(input('Ingrese el tercero número:'))
c = int(input('Ingrese el segundo número:'))

x = min(a, b, c)
y = max(a, b, c)
z = (a + b + c) - x - y

print('{}, {}, {}'.format(x, z, y))
