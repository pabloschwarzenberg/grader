#Aprobación de créditos
ingreso=int(input("Ingreso:"))
nac=int(input("Año de nacimiento:"))
hijos=int(input("Número de hijos:"))
banco=int(input("Años de pertenencia al banco:"))
est=input("Estado civil (S/C):")
lugar=input("Vive en campo o cuidad (U/R):")
if((banco>10)and(hijos>=2)):
  print("APROBADO")
elif((est=="C")and(hijos>3)and(45<=(2018-nac)<=55)):
  print("APROBADO")
elif((ingreso>2500000)and(est=="S")and(lugar=="U")):
  print("APROBADO")
elif((ingreso>3500000)and(banco>5)):
  print("APROBADO")
elif((lugar=="R")and(est=="C")and(hijos<2)):
  print("APROBADO")
else:
  print("RECHAZADO")