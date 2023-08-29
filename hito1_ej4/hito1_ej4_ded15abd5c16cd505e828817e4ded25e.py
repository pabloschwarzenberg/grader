#Conversión de Decimal a Binario
import math
n=int(input())
resto=0
while n//2!=0:
    m=int(math.log2(n))
    resto1=int(10**m)
    resto=resto1+resto
    n=n-(2**m)
if n%2==0:
    print("resultado=",resto)
else:
    print("resultado=",resto+1)
