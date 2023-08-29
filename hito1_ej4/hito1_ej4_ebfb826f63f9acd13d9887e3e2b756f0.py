#Conversión de Decimal a Binario
def decimalToBinary(n):
    return bin(n).replace("0b", "")
n = int(input("ingrese el numero a ser convertido: "))
dec_val = n
print(decimalToBinary(dec_val))