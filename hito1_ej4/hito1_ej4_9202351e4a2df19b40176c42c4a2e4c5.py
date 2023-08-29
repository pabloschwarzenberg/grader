#Conversión de Decimal a Binario
def binario(decimal):
    binar = ''
    while decimal // 2 != 0:
        binar = str(decimal % 2) + binar
        decimal = decimal // 2
    return str(decimal) + binar

numero = int(input('Introduce el número decimal: '))
print('resultado=', binario(numero))