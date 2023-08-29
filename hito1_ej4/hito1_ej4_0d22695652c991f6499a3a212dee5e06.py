#Conversión de Decimal a Binario
# Solicitar número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = bin(numero_decimal)[2:]

# Imprimir el resultado
print("Resultado =", numero_binario)   