#Ordenar tres números
x = int(input('Escriba el primer número: '))
y = int(input('Escriba el segundo número: '))
z = int(input('Escriba el tercer número: '))

a = min(x, y, z)
c = max(x, y, z)
b = (x + y + z) - a - c


print('Los números ordenados son: {}, {} , {}'.format(a,b,c))    