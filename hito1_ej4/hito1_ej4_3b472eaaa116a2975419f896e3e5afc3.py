#Conversión de Decimal a Binario
n=int(input())
binario=[]
while (n//2)>=1:
    resto=n%2
    n=n//2
    binario.append(resto)
binario.append(1)
binario.reverse()
num=""

for n in binario:
    num=num + str(n)
num=int(num)

print("resultado =",num)
        