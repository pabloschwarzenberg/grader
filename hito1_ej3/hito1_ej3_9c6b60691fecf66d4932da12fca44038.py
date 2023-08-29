i=int(input("Ingresos:"))
an=int(input("Año nac:"))
n=int(input("numero hijos:"))
ab=int(input("anosbanco:"))
e=input("estadocivil:")
c=input("campociu:")
if an>10 and n>=2:
 print("APROBADO")
elif e=="C" and n>3 and (an<1971 and an>1961):
 print("APROBADO")
elif i>2500000 and e=="S" and c=="U":
 print("APROBADO")
elif i>3500000 and a>5:
 print("APROBADO")
elif c=="R" and e=="C" and n<2:
 print("APROBADO")
else:
 print("RECHAZADO")