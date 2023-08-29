#Conversión de Decimal a Binario
def intTObin(entero):
    binario = ""
    while entero - 1 != 0:
        if entero % 2 == 0:
            binario += "0"
            entero /= 2
        else:
            binario += "1"
            entero = int(entero / 2)
    binario += "1"
    binario = binario[::-1]