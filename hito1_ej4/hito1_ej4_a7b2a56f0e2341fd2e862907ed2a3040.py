#Conversión de Decimal a Binario
a=int(input())
b=''
while a//2>0:
    b=str(a%2)+ b
    a=a//2
print("resultado=",str(1)+b)