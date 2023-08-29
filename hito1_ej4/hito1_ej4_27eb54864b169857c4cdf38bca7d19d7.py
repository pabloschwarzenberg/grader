#Conversión de Decimal a Binario
a=int(input())

binario=""

while a!=0:
    resto=a%2
    a=a//2
    binario+=str(resto)
    
print("resultado=",binario[::-1])