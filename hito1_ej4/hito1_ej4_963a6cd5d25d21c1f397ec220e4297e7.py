#Conversión de Decimal a Binario
# Obtener el número decimal del usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
binario = bin(numero_decimal)[2:]

# Imprimir el resultado
print("Resultado =", binario)