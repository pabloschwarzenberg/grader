#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    
    return binario

# Pedimos al usuario que ingrese un número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertimos el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimimos el resultado
print("Resultado =", resultado)
