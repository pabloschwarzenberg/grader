dec = 0
numero_decimal = 0
print("Dame un número entero para tranformar a binario:")
dec = int(input())

def dec2bin(decimal):
    bina = ""
    bin(dec)
    bina = int(bin(decimal)[2:])
    return bina

numero_decimal = dec2bin(dec)
print("resultado = {}" .format(numero_decimal))