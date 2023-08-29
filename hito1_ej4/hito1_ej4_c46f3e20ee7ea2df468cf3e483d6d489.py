numero_decimal = int(input(''))

numero_binario = 0
multiplicador = 1

while numero_decimal != 0: # paso 3
    # pasos 1, 4 y 5 se multiplica el módulo por su multiplicador
    numero_binario = numero_binario + numero_decimal % 2 * multiplicador
    numero_decimal //= 2 # paso 1
    multiplicador *= 10 # paso 5

print('resultado =',numero_binario)