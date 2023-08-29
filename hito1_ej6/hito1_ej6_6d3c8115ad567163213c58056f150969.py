#Ordenar tres números
a = int(input('Ingrese un primer número entero: '))
b = int(input('Ingrese un segundo número entero: '))
c = int(input('Ingrese un tercer número entero: '))

x = min(a,b,c)
z = max(a,b,c)
y = (a+b+c) - x - z

print('Los números de menor a mayor son: {}, {}, {}' .format(x,y,z))