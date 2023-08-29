ingreso=int(input())
anodenacimiento=int((input()))
hijos=int(input())
anospertenencia=int(input())
estadocivil=str(input())
vivienda=str(input())
if anospertenencia>10 and hijos>=2:
    print("APROBADO")
elif (estadocivil=="C" and hijos>3) and (anodenacimiento>=1963 and anodenacimiento<=1973):
    print("APROBADO")
elif ingreso>=2500000 and estadocivil=="S" and vivienda=="U":
    print("APROBADO")
elif ingreso>=3500000 and anospertenencia>5 :
    print("APROBADO")
elif vivienda=="R" and estadocivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")