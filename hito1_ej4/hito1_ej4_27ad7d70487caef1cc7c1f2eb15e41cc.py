#Conversión de Decimal a Binario
numero = int(input('ingrese un valor: '))
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
print("resultado=",binarizar(numero))