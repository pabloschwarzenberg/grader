#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario usando la función bin()
numero_binario = bin(numero_decimal)

# Extraer el resultado binario como una cadena de texto y eliminar el prefijo "0b"
resultado = numero_binario[2:]

# Imprimir el resultado
print("resultado =", resultado)
    