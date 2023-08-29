print('Introduce el número: ')
numero = int(input ())

M = numero / 1000
tmp = numero % 1000

C = tmp / 100
tmp = tmp % 100
D = tmp / 10
U = tmp % 10

print('Unidades de millar: %i' % M)
print('Centenas: %i' % C)
print('Decenas: %i' % D)
print('Unidades: %i' % U)

# CONCATENAR
print('%i' % M, 'M', '+' , '%i' % C, 'C', '+' , '%i' % D, 'D', '+', '%i' % U, 'U')