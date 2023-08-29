#Descomponer un número
numero=int(input("Introduce un numero:"))

MC= numero/1000
tmp= numero%1000

CC=tmp/100
tmp=tmp%100

DC=tmp/10
UC=tmp%10

M=int(MC)
C=int(CC)
D=int(DC)
U=int(UC)
print(M,"M","+",C,"C","+",D,"D","+",U,"U")     