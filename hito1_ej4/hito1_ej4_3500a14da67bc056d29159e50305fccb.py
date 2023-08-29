#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = bin(numero_decimal)
resultado = numero_binario[2:]
print("resultado =", resultado)