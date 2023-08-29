#Conversión de Decimal a Binario
n=int(input())
a= str()
while n > 0:
    a = a+str(n%2)
    n = n//2
    print("resultado=",a[::-1])