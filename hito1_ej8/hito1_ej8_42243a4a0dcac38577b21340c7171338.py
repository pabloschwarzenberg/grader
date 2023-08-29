#Descomponer un número
numero=int(input("ingrese un numero: "))
M=numero//1000
C=(M//1000)%100
D=(C//100)%10
U=(D//10)%1
print(M,C,D,U)
