def decimal_a_binario(numero):
    resultado = bin(numero)[2:]  # Convierte a binario y elimina el prefijo "0b"
    return resultado

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", numero_binario)
