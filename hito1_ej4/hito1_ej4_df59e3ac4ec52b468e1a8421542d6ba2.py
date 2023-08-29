#Conversión de Decimal a Binario
def binarizar(dec):
    bin = ''
    while dec // 2 != 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return str(dec) + bin

numero = int(input('Introduce el número a convertir binario: '))
print("resultado="+str(binarizar(numero)))