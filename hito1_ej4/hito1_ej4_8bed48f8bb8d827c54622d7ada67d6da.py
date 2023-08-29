#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    
    return binario

# Pedir al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado)
      