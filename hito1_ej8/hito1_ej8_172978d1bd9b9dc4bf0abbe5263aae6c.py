#Descomponer un número
# Descomponer un número

# Escribe un programa que le pida al usuario un número de hasta 4 dígitos
# y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles. Ejemplos

# Ejemplo: Para 1230 debe imprimir: 1M + 2C + 3D + 0U
# Ejemplo: Para 36 debe imprimir: 3D + 6U

# =================================

print('Introduce el número: ')
numero = int(input ())

M = numero / 1000
tmp = numero % 1000

C = tmp / 100
tmp = tmp % 100
D = tmp / 10
U = tmp % 10

# print('Unidades de millar: %i' % M)
# print('Centenas: %i' % C)
# print('Decenas: %i' % D)
# print('Unidades: %i' % U)

# CONCATENAR
print('%i' % M, 'M', '+' , '%i' % C, 'C', '+' , '%i' % D, 'D', '+', '%i' % U, 'U     