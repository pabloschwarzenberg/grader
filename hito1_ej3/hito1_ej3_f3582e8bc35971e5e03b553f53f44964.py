#Aprobación de créditos
ingreso=int(input())
anonac=int(input())
hijos=int(input())
anobanco=int(input())
estadocivil=input()
vive=input()
if anobanco>10 and hijos>=2:
    print("APROBADO")
elif estadocivil=="C" and hijos>3 and 45<(2018-anonac)<55:
    print("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and anobanco>5:
    print("APROBADO")
elif vive=="R" and estadocivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")     