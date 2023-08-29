#Conversión de Decimal a Binario
n = int(input())

a=0
b=""
while n>0:
        a=n%2
        b+=str(a)
        n=n//2
c=b[::-1]
print("resultado="+c)
        