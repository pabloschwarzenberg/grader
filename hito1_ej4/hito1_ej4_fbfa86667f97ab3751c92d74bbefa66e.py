#Conversión de Decimal a Binario
numero = float(input("dame un numero: "))
numero = bin(round(numero))
print("resultado =", numero[2:])      