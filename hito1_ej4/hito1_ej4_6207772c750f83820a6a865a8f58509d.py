#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Convertir el decimal a binario omitiendo los primeros dos caracteres '0b'
    return binario

# Obtener el número decimal del usuario
decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(decimal)

# Mostrar el resultado
print("resultado=" + resultado)
