# se perdirán 3 número y se rdenarán de mayor a menor
A=int(input("ingrese el primer numero: "))
B=int(input("ingrese el segundo número: "))
C=int(input("ingrese el tercer número: "))
if A<=B<=C:
    print(str(A) + (",") + str(B) + (",") + str(C))
elif A<=C<=B:
    print(str(A) + (",") + str(C) + (",") + str(B))
elif B<=A<=C:
    print(str(B) + (",") + str(A) + (",") + str(C))
elif B<=C<=A:
    print(str(B) + (",") + str(C) + (",") + str(A))
elif C<=A<=B:
    print(str(C) + (",") + str(A) + (",") + str(B))
else:
    if C<=B<=A:
        print(str(8) + (",") + str(B) + (",") + str(A))