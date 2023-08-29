#Conversión de Decimal a Binario
def binarizar(dec):
    binario = ''
    while dec // 2 != 0:
        binario = str(dec % 2) + binario
        dec = dec // 2
    return str(dec) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print("resultado=",binarizar(numero))      