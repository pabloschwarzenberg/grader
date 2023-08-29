#Conversión de Decimal a Binario
# Solicitar al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario
numero_binario = bin(numero_decimal)[2:]

# Imprimir el resultado
print("resultado =", numero_binario)
      