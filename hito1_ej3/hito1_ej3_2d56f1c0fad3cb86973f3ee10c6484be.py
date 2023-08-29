#Aprobación de créditos
I=int(input())
A=int(input())
H=int(input())
AB=int(input())
E=input()
V=input()
if 10<=AB and 2<=H:
   print("APROBADO")
elif E=="C" and 3<H and 45<A<55:
    print ("APROBADO")
elif 3500000<I and 5<=AB:
    print("APROBADO")
elif 2500000<I and E=="S" and V=="R":
    print("APROBADO")
elif V=="R" and E=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")