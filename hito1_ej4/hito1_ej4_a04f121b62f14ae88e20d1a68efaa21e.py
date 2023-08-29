#Conversión de Decimal a Binario
decimal=int(input())
n=0
suma=0
while decimal>=1:
    resto=(decimal%2)*10**n
    suma+=resto
    decimal=decimal//2
    n+=1
    
print("resultado=",suma)
