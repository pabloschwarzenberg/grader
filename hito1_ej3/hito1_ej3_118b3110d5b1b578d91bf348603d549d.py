#Aprobación de créditos
import datetime
ing = eval(input("Mencione sus ingreseos(en pesos):"))
ano = int(input("Ingrese su año de nacimiento:"))
num_h = int(input("Ingrese número de hijos que tiene:"))
ano_b = int(input("Ingrese sus años de pertencia al banco:"))
ec = str(input("Ingrese estado civil(S: soltero, C: casado)"))
viv = str(input("Ingrese si vive en campo o cuidad (U: urbano, R: rural)"))

if ano_b>10 and num_h>=2:
  print("APROBADO")
if ec[0]=="C" and num_h>3 and 45<(2020-ano)<55:
  print("APROBADO")
if ing>2500000 and ec[0]=="S" and viv[0]=="U":
  print("APROBADO")
if ing>3500000 and ano_b>5:
  print("APROBADO")
if viv[0]=="R" and ec[0]=="C" and num_h<2:
  print("APROBADO")
else:
  print("RECHAZADO")

