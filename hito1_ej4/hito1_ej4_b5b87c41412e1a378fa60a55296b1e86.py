#Conversión de Decimal a Binario
 def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return float(decimal) + binario

numero = int(input('Pon un numero y se tranformara en un numero binario: '))
print(binarizar(numero))     