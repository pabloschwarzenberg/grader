n=input("ingrese numero: ")
n=str(n)
if len(n)==4:
    M=n[0]
    C=n[1]
    D=n[2]
    U=n[3]
    print(M,"M +",C,"C +",D,"D +",U,"U")
elif len(n)==3:
    C1=n[0]
    D1=n[1]
    U1=n[2]
    print(C1,"C+",D1,"D+",U1,"U")
elif len(n)==2:
    D2=n[0]
    U2=n[1]
    print(D1,"D+",U1,"U")

elif len(n)==1:
    U3=n[0]
    print(U3)
      