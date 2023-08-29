#Conversión de Decimal a Binario
#ENTRADA
numero = int(input('Ingrese el número decimal: '))

#DESARROLLO
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

#SALIDA
print("Su numero binario es:",(binarizar(numero))) 
numero = int(input("ingrese numero entero: "))
binario= bin(numero)[2:]
print("resultado=", binario)