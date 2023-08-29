#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    resultado = ""
    
    if numero == 0:
        resultado = "0"
    
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2
    
    return resultado

# Solicitar al usuario el número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado_binario)      