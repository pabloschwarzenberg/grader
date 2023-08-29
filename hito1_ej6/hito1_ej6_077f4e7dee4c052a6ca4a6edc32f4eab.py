#Ordenar tres números
x= int(input('escriba el primer número: '))
y= int(input('escriba el segundo número: '))
z= int(input('escriba el tercer número: '))

a = min(x, y, z)
b = max(x, y, z)
c = (x + y + z) - a - b

print('Los números ordenados de menor a mayor son: {},{},{}'.format(a,c,b))