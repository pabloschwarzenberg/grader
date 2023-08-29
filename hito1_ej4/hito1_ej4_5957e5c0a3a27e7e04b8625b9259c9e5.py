#Conversión de Decimal a Binario
N =int(input("Ingrese el numero a convertir: "))

def binarizar(X):

    A = ''
    while X//2!=0:
        A =str(X % 2)+A
        X =X//2
    return str(X)+A

print("resultado=",binarizar(N))