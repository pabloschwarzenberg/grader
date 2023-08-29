#Conversión de Decimal a Binario
def binarizar(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    
numero = int(input("Introduce el numero que deseas transformar a binario"))
binario = binarizar(numero)
binario = int(binario)
print("resultado={}".format(binario))