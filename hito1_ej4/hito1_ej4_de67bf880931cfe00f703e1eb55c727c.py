#Conversión de Decimal a Binario
number=int(input())
large=len(str(number))
binario=str(input())
while large>0:
   a=number%2
   b=str(a)
   c=number//2
   binario+=b
   number=c
   if c<10**(large-1):
      large-=1
print('Resultado='+binario[::-1])