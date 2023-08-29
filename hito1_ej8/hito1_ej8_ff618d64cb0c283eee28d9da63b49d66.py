#Descomponer un número
numero = int(input ())

M= numero // 1000
tmp = numero % 1000

C= tmp // 100
tmp = tmp % 100
D= tmp // 10
U= tmp % 10

print(str(M)+"M+"+str(C)+"C+"+str(D)+"D+"+str(U)+"U ")
 


