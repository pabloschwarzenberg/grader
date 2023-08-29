#Conversión de Decimal a Binario
decimal = int(input('Ingrese el número que desea transformar: '))
binario = bin(decimal)[:2]

print(binario)