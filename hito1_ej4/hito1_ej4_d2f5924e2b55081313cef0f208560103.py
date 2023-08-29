#Conversión de Decimal a Binario
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input("Ingrese el número que desea convertir a binario: "))
print("resultado=",binarizar(numero))