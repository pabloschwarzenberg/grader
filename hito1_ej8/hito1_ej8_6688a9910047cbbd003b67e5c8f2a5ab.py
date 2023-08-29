#Descomponer un número
N=int(input("Ingrese su numero: "))

a=N//10
b=N//100
c=N//1000

if (a==0):
    nim=str(N)
    U=nim[0]
    print(U + "U")
elif(b==0):
    num=str(N)
    U1=(num[1])
    D1=(num[0])
    print(D1 + "D","+",U1 +  "U")
elif(c==0):
    nom=str(N)
    U2=(nom[2])
    D2=(nom[1])
    C=(nom[0])
    print(C + "C","+",D2 + "D","+",U2 + "U")
else:
    nem=str(N)
    U3=nem[3]
    D3=nem[2]
    C2=nem[1]
    M=nem[0]
    print(M + "M","+",C2 + "C","+",D3 + "D","+",U3 + "U")   