#Descomponer un número
numero=int(input())

M=numero//1000
x=numero%1000

C=x//100

y=x%100

D=y//10

U=y%10

print(str(M)+"M+"+str(C)+"C+"+str(D)+"D+"+str(U)+"U")