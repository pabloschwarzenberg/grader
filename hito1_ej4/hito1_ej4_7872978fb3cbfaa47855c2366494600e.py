#Conversión de Decimal a Binario
x = int(input("numero: "))

def bi(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

y = bi(x)

print("resultado="+y)