#Descomponer un número
numero=int(input("Ingrese un numero: "))
while not(numero>=1 and numero<9999):
    numero=int(input("Intentalo denuevo, ingrese un numero: "))
    
largo=len(str(numero))

if largo==4:
    M=str(numero)[0]
    C=str(numero)[1]
    D=str(numero)[2]
    U=str(numero)[-1]
    print(M,"M+",C,"C+",D,"D+",U,"U")


if(largo==3):
        C=str(numero)[0]
        D=str(numero)[1]
        U=str(numero)[-1]
        print(C,"C+",D,"D+",U,"U")
    
if (largo==2):
        D=str(numero)[0]
        U=str(numero)[-1]
        print(D,"D+",U,"U")
if (largo==1):
    U=str(numero)[0]
    print(U,"U")
