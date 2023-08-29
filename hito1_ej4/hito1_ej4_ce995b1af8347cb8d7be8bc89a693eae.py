#Conversión de Decimal a Binario
n=int(input())
aux=''
while n!=0:
    if n%2==1:
        aux='1'+aux
        n=n//2
    else:
        aux='0'+aux
        n=n//2
print('resultado=',aux)
