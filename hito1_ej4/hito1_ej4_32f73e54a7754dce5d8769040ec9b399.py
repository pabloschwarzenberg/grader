#Conversión de Decimal a Binario

def labinarizacion(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce un número: '))
print('resultado','=',labinarizacion(numero))