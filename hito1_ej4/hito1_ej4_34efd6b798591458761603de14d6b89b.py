#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    # Comprobamos si el número es cero
    if numero == 0:
        return '0'

    binario = ''
    # Realizamos la conversión a binario mediante divisiones sucesivas
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2

    return binario

# Pedimos al usuario que ingrese el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertimos el número decimal a binario
resultado = decimal_a_binario(decimal)

# Imprimimos el resultado
print("Resultado =", resultado)
      