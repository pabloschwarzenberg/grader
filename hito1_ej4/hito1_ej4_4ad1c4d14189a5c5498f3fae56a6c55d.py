#Conversión de Decimal a Binario
print('** CONVERTIR DECIMAL A BINARIO **')
def binario(numero):
    binario = ''
    while numero // 2 != 0:
        variable = numero % 2
        binario = str(variable) + binario
        numero = numero // 2
    final = str(numero) + binario
    return final

n = int(input())
print('resultado='+binario(n))  