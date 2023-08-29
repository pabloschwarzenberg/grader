#Descomponer un número
n=int(input())
if n>=1000:
   a=n//1000
   b=(n%1000)//100
   c=(n%100)//10
   d=(n%10)//1
   print(a,"M","+",b,"C","+",c,"D","+",d,"U")
if n<1000:
   b=n//100
   c=(n%100)//10
   d=(n%10)//1
   print(b,"C","+",c,"D","+",d,"U")
if n<100:
   c=n//10
   d=(n%10)//1
   print(c,"D","+",d,"U")
if n<10:
   d=n//1
   print(d,"U")
else:
   print("Las cifras del numero han excedido el límite")

