#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = ""
    
    # Manejo de caso especial cuando el decimal es 0
    if decimal == 0:
        return "0"
    
    # Realizar la conversión a binario
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    
    return binario

# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado)
     