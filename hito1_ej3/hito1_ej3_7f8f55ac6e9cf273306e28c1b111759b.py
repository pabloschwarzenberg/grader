#Aprobación de créditos
ingreso=int(input())
ano=int(input())
hijos=int(input())
anosbanco=int(input())
estadocivil=input()
vive=input()
if anosbanco>10 and hijos>=2 :
 print("APROBADO")
elif estadocivil=="C" and hijos>3 and 1963<ano<1973 :
 print("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and vive=="U" :
 print("PROBADO")
elif ingreso>3500000 and anosbanco>5 :
 print("APROBADO")
elif vive=="R" and estadocivil=="C" and hijos<2 :
 print("APROBADO")
else:
    print("RECHAZADO")
