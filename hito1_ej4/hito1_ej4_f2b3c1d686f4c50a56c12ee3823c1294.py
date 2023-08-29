#Conversión de Decimal a Binario
def binario(decimal):
    binario = ''

    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

decimal_convertir = int(input('Ingrese el numero a convertir: '))
binario_convertido = binario(decimal_convertir)

print('resultado =', binario_convertido)
