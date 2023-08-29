#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Utilizamos la función bin() para obtener el número binario y omitimos los dos primeros caracteres "0b"
    return binario

# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", numero_binario)
      