#Conversión de Decimal a Binario
def convertir(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

n = int(input('Introduce el número a convertir a binario: '))
print('resultado=',(convertir(n)))