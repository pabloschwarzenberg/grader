#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

# Solicitar al usuario el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(decimal)

# Imprimir el resultado
print("resultado =", resultado)
      