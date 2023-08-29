#Conversión de Decimal a Binario
numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = bin(numero_decimal)[2:]
res = ("resultado=")
print(res + numero_binario)