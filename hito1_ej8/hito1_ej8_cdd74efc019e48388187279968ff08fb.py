#Descomponer un número
#preguntar para que cuente las letras hacia el otro lado.
#falta quitar el espacio entre las letras.
a=(input("inserte un número"))
b=int(a)
if b>=1000:
    M=(a[0])
    C=(a[1])
    D=(a[2])
    U=(a[3])
    int(M)
    int(C)
    int(D)
    int(U)
    print(M+"M+",C+"C+",D+"D+",U+"U")
    
elif 100<=b<1000:
    C=(a[0])
    D=(a[1])
    U=(a[2])
    int(C)
    int(D)
    int(U)
    print(C+"C+",D+"D+",U+"U")

elif 10<=b<100:
    D=(a[0])
    U=(a[1])
    int(D)
    int(U)
    print(D+"D+",U+"U")

elif 10<=b<100:
    U=(a[0])
    int(U)
    print(U+"U")
