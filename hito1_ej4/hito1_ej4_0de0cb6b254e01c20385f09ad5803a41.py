#Conversión de Decimal a Binario
numero = input("Ingrese un numero: ")
numero_decimal = int(numero)
numero_binario = bin(numero_decimal)
binario = numero_binario[2:]
print("resultado=",binario)