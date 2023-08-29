#Conversión de Decimal a Binario
def binariodec(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce número a convertir a binario: '))
print('resultado=', binariodec(numero))