a = int(input('Escriba el primer número entero: '))
b = int(input('Escriba el segundo número entero: '))
c = int(input('Escriba el tercer número entero: '))

x = min(a, b, c)
d = max(a, b, c)
n = (a + b + c) - x - d 

print('Los números ordenados serian: {}, {} y {}'.format(x, n, d))