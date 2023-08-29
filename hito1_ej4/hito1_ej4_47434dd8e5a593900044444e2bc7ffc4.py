#Conversión de Decimal a Binario
n=int(input())
resto=""
while n>1:
    resto=str(n%2)+resto
    n=n//2
print("resultado=",str(n)+resto)
