A = int(input("ingrese un numero: "))
B = str(A)
B = len(B)
B = int(B)
if B == 4:
    A = str(A)
    B = A[0]
    C = A[1]
    D = A[2]
    E = A[3]
    print (B+"M","+",C+"C","+",D+"D","+",E+"U")
elif B==3:
    A = str(A)
    B = A[0]
    C = A[1]
    D = A[2]
    print (B+"C","+",C+"D","+",D+"U")
elif B==2:
    A = str(A)
    B = A[0]
    C = A[1]
    print (B+"D","+",C+"U")
elif B==1:
    A = str(A)
    B = A[0]
    print (B+"U")
else:
    print("Error")