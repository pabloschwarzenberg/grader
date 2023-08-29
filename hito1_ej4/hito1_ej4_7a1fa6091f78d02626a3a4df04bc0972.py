#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Usamos la función bin() para convertir a binario y eliminamos el prefijo '0b'
    return binario

# Solicitar el número decimal al usuario
decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(decimal)

# Imprimir el resultado
print("resultado =", resultado)
      