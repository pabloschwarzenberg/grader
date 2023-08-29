#Descomponer un número

import math

a=int(input())

m=a/1000
c=(a/100)%10
d=(a%100)//10
u=a%10

if m<1:
    print(math.floor(c),"C +",d,"D +",u,"U")
elif m<1 and c<1:
    print(d,"D +",u,"U")
else:
    print("Numero 1:",math.floor(m),"M +",math.floor(c),"C +",d,"D +",u,"U")
