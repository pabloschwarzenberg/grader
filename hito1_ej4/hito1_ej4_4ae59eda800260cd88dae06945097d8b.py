#Conversión de Decimal a Binario
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario      
decimal=eval(input("Ingrese decimal: ")
decimal.binarizar(decimal)
print(decimal)

