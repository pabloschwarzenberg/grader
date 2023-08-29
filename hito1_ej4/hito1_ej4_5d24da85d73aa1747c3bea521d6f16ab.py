#Conversión de Decimal a Binario
binario = ""
n=int(input())
while n>0:
    if n%2==0:
        binario = binario + "0"
    elif n%2==1:
        binario=binario + "1"
    n=n//2
print("resultado= ",binario[::-1])