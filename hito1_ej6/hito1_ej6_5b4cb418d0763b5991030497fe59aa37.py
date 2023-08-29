#Ordenar tres números
x = int(input('Primer numero: '))
y = int(input('Segundo numero: '))
z = int(input('Tercer numero: '))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print('Los numeros de menor a mayor son : {} ,{},{}'. format(a, b, c))