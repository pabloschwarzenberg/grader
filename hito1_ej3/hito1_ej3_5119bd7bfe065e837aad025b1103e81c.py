#Aprobación de créditos
ing=int(input("Ingresos:"))
anonac=int(input("Año nac:"))
nhijos=int(input("numero hijos:"))
anosban=int(input("anosbanco:"))
estado=input("estadocivil:")
campociu=input("campociu:")
if anosban>10 and nhijos>=2:
 print("APROBADO")
elif estado=="C" and nhijos>3 and (anonac<1971 and anonac>1961):
 print("APROBADO")
elif ing>2500000 and estado=="S" and campociu=="U":
 print("APROBADO")
elif ing>3500000 and anosban>5:
 print("APROBADO")
elif campociu=="R" and estado=="C" and nhijos<2:
 print("APROBADO")
else:
 print("RECHAZADO")