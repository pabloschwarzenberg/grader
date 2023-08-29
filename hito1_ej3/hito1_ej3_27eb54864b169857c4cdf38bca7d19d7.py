#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
estadocivil=input()
vive=input()
if pertenencia>=10 and hijos>=2:
    print("APROBADO")
elif estadocivil=="C" and hijos>=3 and nacimiento<=1975 and nacimiento>=1963:
    print("APROBADO")
elif ingreso>=2500000 and estadocivil=="S" and vive=="U":
    print("APROBADO")
elif ingreso>=3500000 and pertenencia>=5:
    print("APROBADO")
elif vive=="R" and estadocivil=="C" and hijos<=2:
    print("APROBADO")
else: 
    print=("RECHAZADO")