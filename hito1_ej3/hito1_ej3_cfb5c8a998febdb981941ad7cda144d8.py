#Aprobación de Créditos
I= int(input())
A= int(input())
H= int(input())
B= int(input())
E= input()
V= input()
if B>10 and H>=2:
    print("APROBADO")
elif E=="C" and H>3 and 1962<=A<=1972:
    print("APROBADO")
elif I>2500000 and E=="S" and V=="U":
    print("APROBADO")
elif I>3500000 and B>5:
    print("APROBADO")
elif V=="R" and E=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")