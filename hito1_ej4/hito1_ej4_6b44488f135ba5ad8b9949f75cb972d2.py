#Conversión de Decimal a Binario
n=int(input())
b=""
while n>0:
    if n==1:
        b="1"+b
        break
    elif n%2==0:
        b="0"+b
    else:
        b="1"+b
    n=n//2

print("resultado=",b)