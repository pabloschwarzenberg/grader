#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut:"))
d=(rut//10000000) * 3
f=((rut//1)%10) * 2
g=((rut//10)%10) * 3
h=((rut//100)%10) * 4
j=((rut//1000)%10) * 5
k=((rut//10000)%10) * 6
l=((rut//100000)%10) * 7
u=((rut//1000000)%10) * 2
T=(d+f+g+h+j+k+l+u)
S1=T//11
S2=T-(11*S1)
P=11-S2
if P == 11:
    print("dv=",end="")
    print("0")
else:
    if P == 10:
        print("dv=", end="")
        print("k")
    else:
        print("dv=",end="")
        print(P)
