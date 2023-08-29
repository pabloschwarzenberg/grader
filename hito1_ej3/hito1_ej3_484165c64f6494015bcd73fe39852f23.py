#Aprobación de créditos
ingresos= int(input("ingresos: "))
anno= int(input("año: "))
hijos= int(input("hijos: "))
anosb= int(input("convenio banco: "))
estado= str(input("estado civil s o c: "))
viviend= str(input("vivienda r o u: "))

edad= 2022-anno
estadoc= estado.upper()
vivienda= viviend.upper()
if anosb>10 and hijos>2:
  print("CREDITO APROBADO")
elif estadoc=="C" and hijos>3 and 45<=edad>=55:
  print("CREDITO APROBADO")
elif ingresos >= 2500000 and estadoc=="S" and vivienda== "U":
  print("CREDITO APROBADO")
elif ingresos >= 3500000 and anosb > 5 : 
  print("CREDITO APROBADO")
elif vivienda== "R" and estadoc=="C" and hijos<2:
  print("CREDITO APROBADO")
else:
  print("CREDITO RECHAZADO")