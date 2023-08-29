#Aprobación de créditos
salario= int(input("ingrese su Ingreso: "))
linaje=int(input("ingrese año de linaje: "))
pupilos=int(input("ingrese numero de pupilos: "))
propiedad=int(input("ingrese años de propiedad en el banco: "))
estadocivil=input("ingrese Estado civil  S: soltero C, casado: ")
dondesesitua=input("ingrese Si se situa en campo o cuidad U: urbano, R: rural R: ")
edad=2021-linaje
if (propiedad > 10 ) and (pupilos > 2):
  print("APROBADO")
elif(estadocivil=="C")and(pupilos>3)and((edad>=45)and(edad<=55)):
  print("APROBADO")
elif(estadocivil=="S")and(dondesesitua=="U")and(salario>=25000000):
 print("APROBADO")
elif(propiedad>=5)and(salario>=35000000):
  print("APROBADO")
elif(dondesesitua=="R")and(pupilos<=2):
  print("APROBADO")
else:
  print("RECHAZADO")      