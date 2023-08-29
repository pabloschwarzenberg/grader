#Conversión de Decimal a Binario
numero = int(input("Introduzca el número que quiere convertir a binario: "))

def binarizar(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

print("El número ingresado en lenguaje binario es ", binarizar(numero))      