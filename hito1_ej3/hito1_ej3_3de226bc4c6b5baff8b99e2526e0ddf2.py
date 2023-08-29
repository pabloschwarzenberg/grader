#Aprobación de créditos
I=int(input())
A=int(input())
N=int(input())
P=int(input())
E=str(input())
V=str(input())

if P>10 and N>=2:
    print("APROBADO")

if E== "C" and N>=3 and 45<(2018-A)<55:
    print("APROBADO")

if I>2500000 and E== "S" and V== "U":
    print("APROBADO")

if I>3500000 and P>5:
    print("APROBADO")

if V== "R" and E== "C" and N<2:
    print("APROBADO")

else:
    print("RECHAZADO")      