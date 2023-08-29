numero = int(input('Introduce el número a convertir a binario:'))
def decimal_a_binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


print("resultado=",decimal_a_binario(numero))