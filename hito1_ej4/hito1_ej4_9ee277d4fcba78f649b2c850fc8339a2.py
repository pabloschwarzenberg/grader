def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  # Convierte el número decimal a binario
    return binario

# Solicitar al usuario que ingrese el número decimal
decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(decimal)

# Imprimir el resultado
print("Resultado =", resultado)

      