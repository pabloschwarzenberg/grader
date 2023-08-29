#Conversión de Decimal a Binario
def binarizar(numero):
    binario = ''
    while numero // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario