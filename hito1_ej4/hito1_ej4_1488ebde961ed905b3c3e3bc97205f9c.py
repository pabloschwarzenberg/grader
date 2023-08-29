#Conversión de Decimal a Binario
def db(decimal):
    if decimal <= 0:
        return "0"

    binario = " "

    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario
    
decimal = float(input("ponga un número decimal: "))
binario = db(decimal)


print("resultado="+ binario)