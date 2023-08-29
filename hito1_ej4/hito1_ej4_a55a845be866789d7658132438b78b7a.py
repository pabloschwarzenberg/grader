#Conversión de Decimal a Binario
def decimal_a_binario(numero_decimal):
    if numero_decimal == 0:
        return '0'  # Caso especial para el número decimal 0
    
    binario = ''
    while numero_decimal > 0:
        bit = numero_decimal % 2
        binario = str(bit) + binario
        numero_decimal = numero_decimal // 2
    
    return binario

# Solicitar al usuario un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("El número binario es:", resultado)
     