#Aprobación de créditos
ingreso=int(input())
nace=int(input())
hijos=int(input())
anosb=int(input())
ecivil=str(input())
live=str(input())
aos=2018-nace
if anosb>10 and hijos>=2:
    print("APROBADO")
elif ecivil=="C" and hijos>3 and anos>=45 and anos<=55:
    print("APROBADO")
elif anosb>5 and ingreso>=35000000:
    print("APROBADO")
elif live=="R" and ecivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")