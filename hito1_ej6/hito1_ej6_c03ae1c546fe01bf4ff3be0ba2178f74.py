#Ordenar tres números
A=int(input("Escriba el primer número: "))
B=int(input("Escriba el segundo número: "))
C=int(input("Escriba el tercer número: "))
if A < B:
    if A < C:
        if B < C:
            print(A,",",B,",",C)
        else:
            print(A,",",C,",",B)
    else:
        print(C,",",A,",",B)
else:
    if B<C:
        if A < C:
            print(B,",",A,",",C)
        else:
            print(B,",",C,",",A)
    else:
        print(C,",",B,",",A)
