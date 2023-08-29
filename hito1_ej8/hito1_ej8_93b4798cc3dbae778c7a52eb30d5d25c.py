#Descomponer un número
numero_int=int(input("Numero de maximo 4 digitos:"))
M=numero_int//1000
C=(numero_int%1000)//100
D=((numero_int%1000)%100)//10
U=((numero_int%1000)%100)%10

if M!=0 and C!=0 and D!=0 and U!=0:
    print(M,"M+",C,"C+",D,"D+",U,"U",sep='')

if M==0 and C!=0 and D!=0 and U!=0:
    print(C,"C+",D,"D+",U,"U",sep='')

if M==0 and C==0 and D!=0 and U!=0:
    print(D,"D+",U,"U ",sep='')

if M==0 and C==0 and D==0 and U!=0:
    print(U,"U ",sep='')

if M==0 and C==0 and D==0 and U==0:
    print(0)