#Conversión de Decimal a Binario
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]  # Convierte el número decimal a binario (elimina el prefijo '0b')
    return binary

# Pedir al usuario que ingrese un número decimal
decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
binary = decimal_to_binary(decimal)

# Imprimir el resultado
print("resultado =", binary)
      