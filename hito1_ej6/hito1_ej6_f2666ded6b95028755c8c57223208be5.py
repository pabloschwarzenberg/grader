#Ordenar tres números
A=int(input("Numero A:"))
B=int(input("Numero B:"))
C=int(input("Numero C:"))
T=0
if A>B:
    T=A
    A=B
    B=T

if B>C:
    T=B
    B=C
    C=T
if A>B:
    T=A
    A=B
    B=T
print(A,",",B,",",C)