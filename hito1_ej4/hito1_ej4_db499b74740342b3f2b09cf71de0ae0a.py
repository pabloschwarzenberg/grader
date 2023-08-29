#Conversión de Decimal a Binario
def cifrado(decimal):
    binario = " "
    while decimal // 2 != 0:
        binario = str(decimal  % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
decimal = int(input("introduzca un numero: "))

print("conversion:" ,cifrado(decimal))