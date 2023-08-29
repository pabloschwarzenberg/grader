#Aprobación de créditos
ingreso= int(input("ingrese su Renta: "))
nacimiento=int(input("ingrese año de nacimiento: "))
hijos=int(input("ingrese numero de hijos: "))
pertenencia=int(input("ingrese años de pertenencia en el banco: "))
estadocivil=input("ingrese Estado civil  S: soltero C, casado: ")
dondevive=input("ingrese Si vive en campo o cuidad U: urbano, R: rural R: ")
edad=2021-nacimiento
if (pertenencia > 10 ) and (hijos > 2):
  print("APROBADO")
elif(estadocivil=="C")and(hijos>3)and((edad>=45)and(edad<=55)):
  print("APROBADO")
elif(estadocivil=="S")and(dondevive=="U")and(ingreso>=25000000):
 print("APROBADO")
elif(pertenencia>=5)and(ingreso>=35000000):
  print("APROBADO")
elif(dondevive=="R")and(hijos<=2):
  print("APROBADO")
else:
  print("RECHAZADO")
