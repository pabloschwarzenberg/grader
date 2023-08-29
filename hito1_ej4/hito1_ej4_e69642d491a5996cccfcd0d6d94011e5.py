#Conversión de Decimal a Binario
# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = bin(numero_decimal)[2:]  # Se utiliza [2:] para eliminar el prefijo "0b" del resultado binario

# Imprimir el resultado en binario
print("Resultado =", numero_binario)
