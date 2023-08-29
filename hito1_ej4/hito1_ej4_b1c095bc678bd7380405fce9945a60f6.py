#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Convierte el decimal a binario y elimina el prefijo '0b'
    return binario

# Pedir al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Mostrar el resultado
print("Resultado =", resultado)
      