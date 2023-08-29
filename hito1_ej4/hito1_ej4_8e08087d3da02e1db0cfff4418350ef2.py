#Conversión de Decimal a Binario
# Pedir número decimal al usuario
decimal = int(input("Ingrese un número decimal: "))

# Convertir decimal a binario usando la función bin()
binario = bin(decimal)

# Extraer el resultado de la conversión y eliminar el prefijo "0b"
resultado = binario[2:]

# Imprimir el resultado
print("resultado =", resultado)
      