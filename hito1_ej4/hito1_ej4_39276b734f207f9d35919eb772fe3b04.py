#Conversión de Decimal a Binario
dec = 0
numero_binario = 0
numero_decimal = 0
print("Dame un numero entero para transformar a decimal: ")

dec = int(input())
def bin2dec(binario):
    dec = int(str(binario), 2)
    return dec

def dec2bin(decimal):
    bina = ""
    bin(dec)
    bina = int(bin(33)[2:])
    return bina
numero_decimal = dec2bin(dec)
numero_binario = bin2dec(numero_decimal)
print("numero binario {}" .format(numero_binario))
print("numero decimal {}" .format(numero_decimal))