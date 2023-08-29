#Aprobación de créditos
I=int(input())
AN=int(input())
H=int(input())
A=int(input())
EC=input()
V=input()
if A>10 and H>=2:
    print("APROBADO")
if EC=="C" and H>3 and 1962<AN<1972:
    print("APROBADO")
if I>2500000 and EC=="S" and V=="U":
    print("APROBADO")
if I>3500000 and A>5:
    print("APROBADO")
if V=="R" and EC=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")  