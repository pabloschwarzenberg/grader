#Conversión de Decimal a Binariodef decimal_a_binario(numero):
def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    bits = []
    
    while numero > 0:
        residuo = numero % 2
        bits.insert(0, str(residuo))
        numero = numero // 2
    
    return ''.join(bits)

# Solicitar al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado_binario)

      