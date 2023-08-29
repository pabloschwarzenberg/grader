#Aprobación de créditos
ingreso=int(input("Ingreso (en pesos): "))
nacimiento=int(input("Año de nacimiento: "))
numero_hijos=int(input("Numero de hijos: "))
pertenencia=int(input("Años de pertenencia al banco: "))
estadocivil='s'
while (estadocivil!='S' and estadocivil!='C'):
  estadocivil=(input("Estado civil ('S':soltero, 'C':casado. Utilice MAYUSCULA) "))
vivienda='u'
while (vivienda!='U' and vivienda!='R'):
  vivienda=(input("Vivienda ('U': Urbano, 'R': Rural. Utilice MAYUSCULA)"))

if (pertenencia>10 and numero_hijos>=2):
  print("APROBADO")
  
elif (estadocivil=='C' and numero_hijos>3 and (2022-nacimiento>=45 or 2022-nacimiento<=55)):
  print("APROBADO")
  
elif (ingreso>2500000 and estadocivil=='S' and vivienda=='U'):
  print("APROBADO")

elif (ingreso>3500000 and pertenencia>5):
  print("APROBADO")

elif (vivienda=='R' and estadocivil=='C' and numero_hijos<2):
  print("APROBADO")

else:
  print("RECHAZADO")      