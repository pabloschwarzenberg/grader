#Ordenar tres números
x = int(input('escribe tu 1er numero'))
y = int(input('escribe tu 2do numero'))
z = int(input('escribe el 3er numero'))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c

print('los nummero enteros ordenados de menor a mayor es:{}, {}, {}'. format(a, b, c))      