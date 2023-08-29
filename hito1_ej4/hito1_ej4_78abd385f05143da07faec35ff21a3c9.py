#Conversión de Decimal a Binario
Numero_decimal= int(input("Ingrese un número decimal: "))
numero_binario = bin(Numero_decimal)

resultado = numero_binario[2:]

print("resultado =", resultado)