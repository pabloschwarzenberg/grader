def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # La función bin() convierte a binario, [2:] elimina el prefijo "0b"
    return binario

# Solicitar al usuario el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(decimal)

# Imprimir el resultado
print("Resultado =", resultado)
      