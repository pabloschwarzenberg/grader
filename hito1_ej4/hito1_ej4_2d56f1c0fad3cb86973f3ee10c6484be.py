#Conversión de Decimal a Binario
n=int(input())
r=n%2
binario=str(r)
while 0<=n:
     n=n/2
     r=n%2
     binario=str(r)+binario
     print("resultado=",binario)