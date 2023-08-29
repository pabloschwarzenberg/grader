#Aprobación de créditos
ingreso=int(input("ingreso: "))
nacimiento=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
pertenecencia=int(input("años de pertenencia al banco: "))
estadocivil=input("estado civil: ")
vive=input("donde vive: ")
años=2022-nacimiento
if(pertenecencia>10 and hijos>=2):
 print("APROBADO")
if(estadocivil=="C" and hijos>3 and años<55 and años>45):
 print("APROBADO")
elif(ingreso>2500000 and estadocivil=="S" and vive=="U"):
 print("APROBADO")
elif(ingreso>3500000 and pertenecencia>5):
 print("APROBADO")
elif(vive=="R" and estadocivil=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")      