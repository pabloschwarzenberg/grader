#Descomponer un número
x=int(input('Ingrese un número: '))
y=len(str(x))
M1=(x//1000)
C1=((x-M1*1000)//100)
D1=(x-M1*1000-C1*100)//10
U1=(x-M1*1000-C1*100-D1*10)
M=str(M1)
C=str(C1)
D=str(D1)
U=str(U1)
if M1!=0:
    print(M,'M +',C,'C +',D,'D +',U,'U')
elif M1==0 and C1!=0:
    print(C,'C +',D,'D +',U,'U')
elif M1==0 and C1==0 and D1!=0:
    print(D,'D +',U,'U')
elif M1==0 and C1==0 and D1==0:
    print(U,'U')