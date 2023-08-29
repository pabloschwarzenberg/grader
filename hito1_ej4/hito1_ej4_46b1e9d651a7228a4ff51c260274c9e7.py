#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    # Utilizar la función bin() para convertir el número decimal a binario
    binario = bin(numero)[2:]  # Se omite los primeros dos caracteres '0b'

    return binario


# Pedir al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Llamar a la función para convertir el número a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado_binario)      