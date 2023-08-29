#Conversión de Decimal a Binario
numero = int(input('Introduce el numero decimal para convertirlo en binario: '))
def num_binario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
print("resultado=",num_binario(numero))