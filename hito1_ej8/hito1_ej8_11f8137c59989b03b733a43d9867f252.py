#Descomponer un número
numero=int(input('Escoje tu número: '))
a=numero%1000
U=numero%10
D=int((numero%100)/10)
C=int((numero%1000)/100)
M=int(numero/1000)
print(str(M)+'M'+'+'+str(C)+'C'+'+'+str(D)+'D'+'+'+str(U)+'U')  