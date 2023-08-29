#Descomponer un número
a=int(input("Ingrese un numero entero:"))

M=a//1000
b=a%1000

C=b//100
c=b%100

D=c//10
d=c%10

U=d

print(M,"M","+",C,"C","+",D,"D","+",U,"U")