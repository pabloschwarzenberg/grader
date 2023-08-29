#Aprobación de créditos
ingreso= int(input("ingreso:"))
nacimiento= int(input("nacimiento:"))
hijos= int(input("hijos:"))
antiguedad= int(input("antiguedad:"))
estadocivil= str(input("estado civil:"))
campociudad= str(input("campo o ciudad:"))
edad= 2020- nacimiento
if antiguedad>10 and hijos>=2:
  print ("APROBADO")
elif estadocivil=="C" and hijos>3 and 45<= edad<=55:
  print ("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and campociudad=="U":
  print ("APROBADO")
elif ingreso>3500000 and antiguedad>5:
  print ("APROBADO")
elif campociudad=="R" and estadocivil=="C" and hijos<2:
  print ("APROBADO")
else:
  print ("RECHAZADO")