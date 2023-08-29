def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

numero_decimal = int(input("Ingresa un numero decimal: "))

numero_binario = decimal_a_binario(numero_decimal)

print("resultado =", numero_binario)