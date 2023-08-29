#Aprobación de créditos
ingresarenta= int(input("ingrese su Renta: "))
fechadenacimiento=int(input("ingrese año de nacimiento: "))
hijos=int(input("ingrese numero de hijos: "))
pertenencia=int(input("ingrese años de pertenencia en el banco: "))
estadocivil=input("ingrese Estado civil  S: soltero C, casado: ")
campoociudad=input("ingrese Si vive en campo o cuidad U: urbano, R: rural R: ")
edad=2021-fechadenacimiento
if (pertenencia > 10 ) and (hijos > 2):
  print("APROBADO")
elif(estadocivil=="C")and(hijos>3)and((edad>=45)and(edad<=55)):
  print("APROBADO")
elif(estadocivil=="S")and(campoociudad=="U")and(ingresarenta>=25000000):
 print("APROBADO")
elif(pertenencia>=5)and(ingresarenta>=35000000):
  print("APROBADO")
elif(campoociudad=="R")and(hijos<=2):
  print("APROBADO")
else:
  print("RECHAZADO")      