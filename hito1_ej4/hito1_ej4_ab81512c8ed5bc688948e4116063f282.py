#Conversión de Decimal a Binario
a=int(input())
def binarizar(b):
    binario = ""
    while b//2 != 0:
        binario=str(b%2)+binario
        b=b//2
    return str(b) + binario

print("resultado=",binarizar(a))
