#Conversión de Decimal a Binario
num=int(input())
largo=len(str(num))
binario=""
while largo>0:
   a=num%2
   b=str(a)
   c=num//2
   binario+=b
   num=c
   if c<10**(largo-1):
     largo-=1
print("Resultado="+binario[::-1])