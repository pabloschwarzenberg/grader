#Conversión de Decimal a Binario
decimal=float(input())
n=0
suma=0
while decimal>=1:
    resto=(decimal%2)*10**n
    suma=suma+resto
    decimal=decimal//2
    n=n+1
print("resultado=", suma)