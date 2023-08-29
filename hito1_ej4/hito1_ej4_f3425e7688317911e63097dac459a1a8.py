dec = 0
n_b = 0
n_d = 0
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
n_d = dec2bin(dec)
n_b = bin2dec(n_d)
print("resultado={}" .format(n_d)) 