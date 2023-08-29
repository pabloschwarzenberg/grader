#Aprobación de créditos
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
pertenencia=int(input())
civil=str(input("")).upper()
vivienda=str(input("")).upper()
anos=int(2018-nacimiento)
if pertenencia>=10 and hijos>=2:
  print("APROBADO")
elif (civil=="C") and (hijos>=3) and (45<anos<55):
  print("APROBADO")
elif (ingreso>=2500000) and (civil=="S") and (vivienda=="U"):
  print("APROBADO")
elif (ingreso>=3500000) and (pertenencia>=5):
  print("APROBADO")
elif (vivienda=="R") and (civil=="C") and (hijos<=2):
  print("APROBADO")
else:
  print("RECHAZADO")
