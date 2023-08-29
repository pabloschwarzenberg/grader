#Aprobación de créditos
ingreso=int(input())
anonacimiento=int(input())
hijos=int(input())
anosenbanco=int(input())
estadocivil=str(input())
vivienda=str(input())

if anosenbanco>10 and hijos>=2:
    print("APROBADO")
elif estadocivil=="C" and hijos>3 and 1972>=2017-anonacimiento>=1962:
    print("APROBADO")
elif ingreso > 2500000 and estadocivil=="S" and vivienda=="U":
    print("APROBADO")
elif ingreso > 3500000 and anosenbanco > 5:
    print("APROBADO")
elif vivienda=="R" and estadocivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
