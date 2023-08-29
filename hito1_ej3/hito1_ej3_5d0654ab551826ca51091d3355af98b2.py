#Aprobación de créditos
ingreso=int(input())
ano=int(input())
nhijos=int(input())
anobanco=int(input())
estado=str(input())
vive=str(input())

if anobanco>10 and nhijos>=2:
    print("APROBADO")
elif estado=="C" and nhijos>=3 and 45<ano<55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and anobanco>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and nhijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")