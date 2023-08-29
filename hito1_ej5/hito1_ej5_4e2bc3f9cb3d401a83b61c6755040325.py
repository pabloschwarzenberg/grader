#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el rut: "))
X=(rut//10000000) * 3
C=((rut//1000000)%10) * 2
V=((rut//100000)%10) * 7
B=((rut//10000)%10) * 6
N=((rut//1000)%10) * 5
M=((rut//100)%10) * 4
A=((rut//10)%10) * 3
S=((rut//1)%10) * 2
suma=(X+C+V+B+N+M+A+S)
resto1 = suma // 11
resto2 = suma-(11*resto1)
resta = 11-resto2
if resta == 11:
    print("dv = ",end="")
    print(0)
elif resta == 10:
    print("dv = ",end="")
    print("k")
else:
    print("dv = ",end="")
    print(resta)      