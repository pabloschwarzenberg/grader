#Conversión de Decimal a Binario
num = input("Ingrese un numero: ")
num_decimal = int(num)
num_binario = bin(num_decimal)
binario = num_binario[2:]
print("resultado=",binario)     