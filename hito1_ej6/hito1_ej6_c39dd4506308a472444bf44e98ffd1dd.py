#Ordenar tres números
A=0
B=0
C=0
A=input("ingrese valor N°1:")
B=input("ingrese valor N°2:")
C=input("ingrese valor N°3:")
if A<=B:
    if A<=C:
        if B<=C:
            print(A+","+B+","+C)
        else:
            print(A+","+C+","+B)
    else:
        print(C+","+A+","+B)
elif B<=C:
    if B<=A:
        if C<=A:
            print(B+","+C+","+A)
        else:
            print(B+","+A+","+C)
    else:
        print(A+","+B+","+C)
else:
    print(C+","+B+","+A)