#Ordenar tres números
A=int(input("ESCRIBA EL PRIMER NUMERO: "))
B=int(input("ESCRIBA EL SEGUNDO NUMERO: "))
C=int(input("ESCRIBA EL TERCER NUMERO: "))
if A<B<C:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A ,",", B,"Y", C, "ES:")
    print(A,",",B,",",C)
elif A<C<B:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A,",", B,"Y", C, "ES:")
    print(A, ",", C, ",", B)
elif B<A<C:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A,",", B,"Y", C, "ES:")
    print(B, ",", A, ",", C)
elif B<C<A:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A,",", B,"Y", C, "ES:")
    print(B, ",", C, ",", A)
elif C<A<B:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A,",", B,"Y", C, "ES:")
    print(C, ",", A, ",", B)
elif C<B<A:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A,",", B,"Y", C, "ES:")
    print(C, ",", B, ",", A)
elif A == B < C:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(A, ",", B, ",", C)
elif A == C < B:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(A, ",", C, ",", B)
elif C == B < A:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(C, ",", B, ",", A)
elif C < A == B:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(C, ",", A, ",", B)
elif B < A == C:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(B, ",", A, ",", C)
elif A < B == C:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(A, ",", B, ",", C)
else:
    print("EL ORDEN ASCENDENTE DE LOS NUMEROS", A, ",", B, "Y", C, "ES:")
    print(A, ",", B, ",", C)