#Conversión de Decimal a Binario
def bd(n):
    resto=""
    while n//2!=0:
        resto=str(n%2)+resto
        n=n//2
    return str(n)+resto
n=int(input("Ingrese decimal:"))
print("resultado=",bd(n))      