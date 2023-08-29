#Aprobación de créditos
ingreso=int(input("ingreso en pesos: "))
nacimiento=int(input("ano de nacimiento: "))
hijos=int(input("numero de hijos: ")) 
pertenenciaalbanco=int(input("anos de pertenencia al banco: "))
ecivil=input("estado civil (S: soltero, C: casado):")
vive=input("vive en: Urbano(U)/Rural(R)")
if pertenenciaalbanco>10 and hijos>=2:
  print("APROBADO")
if ecivil=="C" and hijos>3 and 45>=2016-nacimiento>=55:
  print ("APROBADO")
if ingreso>2500000 and ecivil=="S" and vive==U:
  print ("APROBADO")
if ingreso>3500000 and pertenenciaalbanco>5:
  print ("APROBADO")
if vive=="R" and ecivil=="C" and hijos<2:
  print ("APROBADO")
else:
  print ("RECHAZADO")