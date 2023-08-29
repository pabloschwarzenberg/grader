# Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

# Pedir al usuario que ingrese el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = decimal_a_binario(decimal)

# Imprimir el resultado
print("Resultado =",{binario})