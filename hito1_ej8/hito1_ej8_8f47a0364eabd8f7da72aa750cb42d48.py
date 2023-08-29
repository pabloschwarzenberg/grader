#Descomponer un número
n=int(input("Escriba un numero de hasta 4 digitos: "))
a=str((n%10000)//1000)
b=str((n%1000)//100)
c=str((n%100)//10)
d=str((n%10)//1)
e=len(a)+len(b)+len(c)+len(d)

if e==4:
 print(a,"M","+",b,"C","+",c,"D","+",d,"U")

elif e==3:
 print(b,"C","+",c,"D","+",d,"U")
 
elif e==2:
 print(c,"D","+",d,"U")

elif e==1:
 print(d,"U")
