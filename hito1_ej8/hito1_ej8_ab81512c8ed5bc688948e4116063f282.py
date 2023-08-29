#Descomponer un número
n=str(input())
x=len(n)
N=n

if x==4:
    a=(N[0])
    b=(N[1])
    c=(N[2])
    d=(N[3])
    print(a,"M+",b,"C+",c,"D+",d,"U")
if x==3:
    a=(N[0])
    b=(N[1])
    c=(N[2])
    print(a,"C+",b,"D+",c,"U")
if x==2:
    a=(N[0])
    b=(N[1])
    print(a,"D+",b,"U")
if x==1:
    a=(N[0])
    print(a,"U")