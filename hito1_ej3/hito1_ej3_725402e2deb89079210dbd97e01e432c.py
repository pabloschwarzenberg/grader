#Aprobación de créditos
ingreso=float(input("Intrdozuca su ingreso en pesos: "))
ac=int(input("Ingrese su año de nacimiento: "))
hijos=(int(input("Ingrese la cantidad de hijos que tiene: ")))
apertbanco=int(input("Ingrese sus años de pertenencia al banco: "))
ecivil=input("Ingrese su estado civil, si esta solteto marque ""S"" y si esta casado marque ""C"": ")
region=input("Si vive en el campo presione ""R"", si vive en la ciudad presione ""U"": ")
if(apertbanco>10 and hijos>=2):
  print("APROBADO")
elif(ecivil=="C") and (hijos<3) and (ac>=1967 and ac<=1977):
  print("APROBADO")
elif(ingreso>2500000) and (ecivil=="S") and (region=="U"):
  print("APROBADO")
elif(ingreso>3500000) and (apertbanco>5):
  print("APROBADO")
elif(region=="R") and (ecivil=="C") and (hijos>2):
  print("APROBADO")
else:
  print("RECHAZADO")