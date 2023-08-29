#Conversión de Decimal a Binario
def transBinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce un numero: '))
print('resultado = ', transBinario(numero))


