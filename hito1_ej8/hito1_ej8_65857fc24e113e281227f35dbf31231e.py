#Descomponer un número
print('Por favor introduzca un número: ')
numero = int(input ())

M = numero / 1000
tmp = numero % 1000

C = tmp / 100
tmp = tmp % 100
D = tmp / 10
U = tmp % 10

# CONCATENAR
print('%i' % M, 'M', '+' , '%i' % C, 'C', '+' , '%i' % D, 'D', '+', '%i' % U, 'U')     