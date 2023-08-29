ingreso = input('rut (primeros 8 digitos sin puntos): ')
try:
    valor = int(ingreso)
except valueerror:
    exit()

x = len(ingreso)

factor = 2
total = 0

while x > 0:
    x = x - 1
    numero = int(ingreso[x : x + 1])
    total = total + (numero * factor)
    if factor == 7:
        factor = 2
    else:
        factor = factor + 1

modulo = total % 11

validador = 11 - modulo

if validador == 11: validador = 0
if validador == 10: validador = 'K'

print('dv=',validador)