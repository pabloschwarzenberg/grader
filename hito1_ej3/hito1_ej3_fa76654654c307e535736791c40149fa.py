ingreso=int(input())
años=int(input())
hijos=int(input())
banco=int(input())
estado=(input())
vive=(input())

if banco>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and hijos>3 and 1962<=años<=1972:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and banco>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
