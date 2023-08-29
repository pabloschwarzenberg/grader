n=str(input("ingrese un numero: "))
if len(n) == 4:
    M=n[0]+"M"
    C=n[1]+"C"
    D=n[2]+"D"
    U=n[3]+"U"
    print(M,"+",C,"+",D,"+", U)
if len(n) == 3:
    C=n[0]+"C"
    D=n[1]+"D"
    U=n[2]+"U"
    print(C,"+",D,"+", U)
if len(n) == 2:
    D=n[0]+"D"
    U=n[1]+"U"
    print(D,"+", U)
if len(n) == 1:
    U=n[0]+"U"
    print(U)