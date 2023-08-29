#Conversión de Decimal a Binario
def dec_to_bin(x):
    return int(bin(x)[2:])
num = int(input('numero a convertir: '))
print('resultado=', dec_to_bin(num))      