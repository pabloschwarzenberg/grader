#Conversión de Decimal a Binario
numero = int(input('Introduce el número para convertir a binario: '))
def PaBinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
print('resultado=',(PaBinario(numero)))