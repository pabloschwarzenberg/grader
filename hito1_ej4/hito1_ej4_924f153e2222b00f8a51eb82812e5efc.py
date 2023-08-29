#Conversión de Decimal a Binario
n = int(input('Introduce el número: '))

def bi(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    

print("resultado=",bi(n))