#Conversión de Decimal a Binario
import math
n=int(input("ingrese numero decimal"))
b=[]
i=0
p=n
while p>1:
    p=n/2**i
    p = int(math.floor(p))
    r=p%2
    b.append(r)
    i=i+1
print(b)
b.reverse()
print(b)
imprimir=""
a=0
while a<len(b):
    imprimir=imprimir+str(b[a])
    a=a+1
print('resultado='+imprimir)     