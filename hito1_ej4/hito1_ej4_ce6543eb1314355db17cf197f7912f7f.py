dec = 0
numero_binario = 0
numero_decimal = 0
print("Dame un número entero para tranformar a binario:")
dec = int(input())
def bin2dec(binario):
    dec = int(str(binario), 2)
    return dec

def dec2bin(decimal):
    bina = ""
    bin(dec)
    bina = int(bin(decimal)[2:])
    return bina
numero_decimal = dec2bin(dec)
numero_binario = bin2dec(numero_decimal)
print("resultado={}" .format(numero_decimal))