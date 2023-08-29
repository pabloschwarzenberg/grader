x = int(input('Ingrese el primer número: '))
y = int(input('Ingrese el segundo número: '))
z = int(input('Ingrese el primer número: '))

a = min(x,y,z)
c = max(x,y,z)
b = (x + y + z) - a - c

print('{}, {}, {}'. format(a, b, c))