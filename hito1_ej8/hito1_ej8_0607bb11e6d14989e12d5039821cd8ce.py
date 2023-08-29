#Descomponer un número
n=int(input("Ingrese un numero de 4 digitos"))
M=0
C=0
D=0
U=0
while 0<=n-1000:
    n=n-1000
    M=M+1
while 0<=n-100:
    n=n-100
    C=C+1
while 0<=n-10:
    n=n-10
    D=D+1
while 0<=n-1:
    n=n-1
    U=U+1
print(M,"M+",C,"C+",D,"D+",U,"U")