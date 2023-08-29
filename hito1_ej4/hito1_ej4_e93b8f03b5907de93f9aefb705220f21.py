#Conversión de Decimal a Binario
#DECIMALES A BINARIOS
dec= 0
dec= int(input())
numeroDecimal = 0

def dec2bin(decimal):
    bina=""
    bin(dec)
    bina= int(bin(dec)[2:])
    return bina
print("resultado=",dec2bin(dec))