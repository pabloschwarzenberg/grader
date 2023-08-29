pesos=int(input("ingrese su Renta "))
fechadenacimiento=int(input("ingrese año de nacimiento "))
hijo=int(input("ingrese numero de hijos "))
pert=int(input("ingrese años de pertenencia en el banco "))
estadocivil=input("ingrese Estado civil  S: soltero C, casado ")
hogar=input("ingrese Si vive en campo o cuidad U: urbano, R: rural R: ")
edad=2021-fechadenacimiento
if (pert > 10 ) and (hijo > 2):
  print("APROBADO")
elif(estadocivil=="C")and(hijo>3)and((edad>=45)and(edad<=55)):
  print("APROBADO")
elif(estadocivil=="S")and(hogar=="U")and(pesos>=25000000):
 print("APROBADO")
elif(pert>=5)and(pesos>=35000000):
  print("APROBADO")
elif(hogar=="R")and(hijo<=2):
  print("APROBADO")
else:
  print("RECHAZADO")