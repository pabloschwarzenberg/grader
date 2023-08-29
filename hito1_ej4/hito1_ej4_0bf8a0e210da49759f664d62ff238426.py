#Conversión de Decimal a Binario
numero = int(input('Numero: '))

binario = ''

while numero >= 1:
    binario += str(numero % 2)
    numero = int(numero / 2)

resultado = binario[::-1]

print("resultado="+resultado)    