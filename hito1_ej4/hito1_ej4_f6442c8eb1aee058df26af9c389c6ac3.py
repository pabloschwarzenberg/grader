# Conversión de decimal a binario

# Solicitar número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Realizar la conversión a binario
numero_binario = bin(numero_decimal)[2:]

# Imprimir el resultado
print("resultado =", numero_binario)
