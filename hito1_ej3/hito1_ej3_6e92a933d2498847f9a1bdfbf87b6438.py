#Aprobación de créditos
ingreso=int(input("Digite el ingreso del cliente: "))
ano=int(input("Ingrese el año de nacimiento del cliente: "))
hijos=int(input("Ingrese el número de hijos del cliente: "))
perten=int(input("Ingrese los años de pertenencia al banco: "))
estCivil=input("Ingrese el estado civil del cliente\n(S): Soltero\n(C): Casado\n")
vive=input("Ingrese (U) si el cliente vive en un espacio Urbano, (R) para rural\n")

aprueba=False
if(perten>10 and hijos>=2):
  aprueba=True
if(estCivil=="C" and hijos>3 and ano<(2017-45) and ano>(2017-55)):
  aprueba=True
if(ingreso>2500000 and estCivil=="S" and vive=="U"):
  aprueba=True
if(ingreso>3500000 and perten>5):
  aprueba=True
if(vive=="R" and estCivil=="C" and hijos<2):
  aprueba=True

if(aprueba):
  print("APROBADO")
else:
	print("RECHAZADO")      