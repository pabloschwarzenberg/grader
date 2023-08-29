#Descomponer un número
numero=int(input())
numero_4=numero//1000
numero_3=numero%1000
numero_3a=numero_3//100
numero_2=numero%100
numero_2a=numero_2//10
numero_1=numero%10

if(numero_4!=0):
    print(numero_4,"M","+",numero_3a,"C","+",numero_2a,"D","+",numero_1,"U")
if((numero_4)==0):
    if(numero_3a!=0):
       print(numero_3a,"C","+",numero_2a,"D","+",numero_1,"U")
if((numero_4)==0):
    if((numero_3a==0) and (numero_2a!=0)):
        print(numero_2a,"D","+",numero_1,"U")
if((numero_4)==0):
    if((numero_3a==0) and (numero_2a==0)):
        print(numero_1,"U")