A=input("Ingrese el primer número entero: ")
B=input("Ingrese el segundo número entero: ")
C=input("Ingrese el tercer número entero: ")
if A>=B:
    if A>=C:
            if B>=C:
                    print(C,",",B,",",A)
            elif B<=C:
                    print(B,",",C,",",A)
    elif C>=A:
             print(B,",",A,",",C)

elif A<=B:
    if B>=C:
            if A>=C:
                    print(C,",",A,",",B)
            elif A<=C:
                    print(A,",",C,",",B)
    elif C>=B:
            print(A,",",B,",",C)

