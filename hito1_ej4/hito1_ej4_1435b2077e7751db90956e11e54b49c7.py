#Conversión de Decimal a Binario
# Obtener el número decimal del usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario
numero_binario = bin(numero_decimal)[2:]  # El prefijo "0b" no es necesario, se omite con [2:]

# Imprimir el resultado
print("Resultado =", numero_binario)
