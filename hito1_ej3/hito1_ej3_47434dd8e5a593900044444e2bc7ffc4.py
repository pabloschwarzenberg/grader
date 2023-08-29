#Aprobación de créditos
I=int(input())
AN=int(input())
H=int(input())
P=int(input())
EC=input()
V=input()
E=2018-AN
if P>10 and H>=2:
    print("APROBADO")
elif EC=="C" and H>3 and 45<E<55:
    print("APROBADO")
elif I>2500000 and EC=="S" and V=="U":
    print("APROBADO")
elif I>3500000 and P>5:
    print("APROBADO")
elif V=="R" and EC=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")