#Conversión de Decimal a Binario
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + str(binario)
        decimal = decimal // 2
    for str(decimal) + str(binario)

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))