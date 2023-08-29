I=int(input())
B=int(input())
H=int(input())
P=int(input())
Ec=input()
V=input()
if 10<P and 2<=H:
    print("APROBADO")
elif Ec=="C" and 3<H and 1962<=B<=1772:
    print("APROBADO")
elif 2500000<I and Ec=="S" and V=="U":
    print("APROBADO")
elif 3500000<=I and 5<P:
    print("APROBADO")
elif V=="R" and Ec=="C" and H<2:
    print("APROBADO")
else:
    print("RECHAZADO")