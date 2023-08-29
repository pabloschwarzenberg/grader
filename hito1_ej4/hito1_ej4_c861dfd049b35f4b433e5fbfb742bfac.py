#Conversión de Decimal a Binario

print("Dame un numero entero para transforma a decimal: ")
dec = int(input())
def dec2bin(decimal):
    bina = ""
    bin(dec)
    bina = int(bin(dec)[2:])
    return bina
numero_decimal = dec2bin(dec)
print("Resultado: {}".format(numero_decimal))