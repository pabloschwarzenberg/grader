def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'
    
    binario = ''
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    
    return binario

# Ejemplo de uso
numero_decimal = int(input("Ingrese un número decimal: "))

binario_resultante = decimal_a_binario(numero_decimal)
print(binario_resultante)

      