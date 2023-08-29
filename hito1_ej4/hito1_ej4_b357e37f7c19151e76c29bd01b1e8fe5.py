#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = str('')
    while decimal > 0:
        resto = int(decimal %2)
        decimal = int(decimal / 2)
        binario = str(resto) + binario
    return binario

decimal = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(decimal)
print ('resultado=',binario)