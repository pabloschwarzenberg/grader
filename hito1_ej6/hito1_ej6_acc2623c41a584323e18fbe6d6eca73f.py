#Ordenar tres números
A=int(input("Ingrese un número:"))
B=int(input("Ingrese un número:"))
C=int(input("Ingrese un número:"))
L=[A,B,C]
I=0
while I<len(L):
    L[I]=str(L[I])
    I=I+1
S=("," .join(L))
G=sorted(L)
print(G[0],",",G[1],",",G[2])