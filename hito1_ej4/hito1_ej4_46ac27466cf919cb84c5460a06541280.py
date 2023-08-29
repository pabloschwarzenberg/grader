#Conversión de Decimal a Binario
decimal = int(input('ingrese numero decimal'))
binario = bin(decimal)
resultado = binario[2:]
print('resultado=', resultado)

