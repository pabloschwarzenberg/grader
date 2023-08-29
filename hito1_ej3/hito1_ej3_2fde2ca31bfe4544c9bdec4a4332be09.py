ingreso=int(input())
año=int(input())
hijos=int(input())
años=int(input())
estado=input()
vive=input()
añoss=2021-año
if años>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and añoss>45 and añoss<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and años>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")