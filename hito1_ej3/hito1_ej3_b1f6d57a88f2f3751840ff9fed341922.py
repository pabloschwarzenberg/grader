#Aprobación de créditos
ingreso=float(input())
ano_nacimiento=float(input())
g=2018-ano_nacimiento
hijos=float(input())
antiguedad=float(input())
estado=str(input())
C=estado
S=estado
origen=str(input())
R=origen
U=origen
if antiguedad >= 10 and hijos>=2:
  print ("APROBADO")
elif hijos>3 and 45<=g<=55 and estado== C :
  print ("APROBADO")
elif ingreso>= 2500000 and estado==S :
  print ("APROBADO")
elif ingreso>= 3500000 and antiguedad>5 and origen== U :
  print ("APROBADO")
elif origen== R and estado== C and hijos<2 :
  print ("APROBADO")
else:
  print("RECHAZADO")