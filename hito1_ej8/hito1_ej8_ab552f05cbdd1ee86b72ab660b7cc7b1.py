#Descomponer un número
a=int(input())
b=int(a/10)
if a<10:
 print(a,"U")
if a<100:
 print(b,"D+",a%10,"U")
if a<1000:
 print(int(a/100),"C+",int((a%100-a%10)/10),"D+",a%10,"U")
if a<10000 and a>=1000:
 print(int(a/1000),"M+",int((a%1000-a%100)/100),"C+",int((a%100-a%10)/10),"D+",a%10,"U")
