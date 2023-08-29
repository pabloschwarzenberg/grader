#Ordenar tres números
A=int(input("Numero:"))
B=int(input("Numero:"))
C=int(input("Numero:"))
if A>=B>=C:print(C,",",B,",",A)
if A>=C>=B:print(B,",",C,",",A)
if C>=B>=A:print(A,",",B,",",C)
if C>=A>=B:print(B,",",A,",",C)
if B>=A>=C:print(C,",",A,",",B)
if B>=C>=A:print(A,",",C,",",B)

      