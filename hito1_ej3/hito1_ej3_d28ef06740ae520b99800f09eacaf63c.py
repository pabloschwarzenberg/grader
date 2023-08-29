#Aprobación de créditos

IN=int(input("Indique Ingreso en pesos"))
AN=int(input("Indique año de nacimiento"))
NH=int(input("Indique numero de hijos"))
APB=int(input("Indique años de pertenencia al banco"))
EC=str(input("Indique estado civil S/C"))
UR=str(input("Indique si vive en campo o ciudad U/R"))

if APB>10 and NH>2:
  print ("APROBADO")
elif EC=="C" and NH>3 and 1962<=AN<=1972:
  print ("APROBADO")
elif IN>=3500000 and APB>5:
  print ("APROBADO")
elif UR=="R" and EC=="C" and NH<2:
  print ("APROBADO")
else:
  print ("RECHAZADO")