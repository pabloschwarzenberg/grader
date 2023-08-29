#Aprobación de créditos

ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenece=int(input())
civil=str(input())
vive=str(input())

edad=2018-nacimiento

if pertenece>10 and hijos>=2 or civil=="C" and hijos>3 and 45<edad<55 or ingreso>2500000 and civil=="S" and vive=="C" or ingreso>3500000 and pertenece>5 or vive=="R"and civil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")
  
  
  