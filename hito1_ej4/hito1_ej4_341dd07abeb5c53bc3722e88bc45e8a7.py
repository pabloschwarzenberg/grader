#Conversión de Decimal a Binario
n=int(input("Ingresa algún número: "))
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
print("Resultado=",binarizar(n))