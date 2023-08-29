#Descomponer un número
a=int(input())
#a_4= milesima, a_3a= centesima, a_2a= décima, a_1= unidad
a_4=a/1000
a_3=a%1000
a_3a=a_3//100
a_2=a%100
a_2a=a_2//10
a_1=a%10

if(a_4!=0): 
   print(a_4,"M","+",a_3a,"C","+",a_2a,"D","+",a_1,"U")
if((a_4==0) and (a_3a!=0)):
   print(a_3a,"C","+",a_2a,"D","+",a_1,"U")
if((a_4==0) and (a_3a==0) and (a_2a!=0)):
   print(a_2a,"D","+",a_1,"U")
if((a_4==0) and (a_3a==0) and (a_2a==0)):
   print(a_1,"U")