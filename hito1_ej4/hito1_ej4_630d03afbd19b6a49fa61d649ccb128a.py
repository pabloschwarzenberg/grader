#Conversión de Decimal a Binario
def binarizar (decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
numero = eval(input("introduce un numero para pasarlo a binario: "))
print("Resultado= ", binarizar(numero))