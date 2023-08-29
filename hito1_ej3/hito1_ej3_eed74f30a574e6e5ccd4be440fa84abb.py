#Aprobación de créditos
ingr = int(input("Ingreso (en pesos): "))
añoN = int(input("Año de nacimiento: "))
num = int(input("Numero de hjos: "))
añoP = int(input("Años de pertenencia al banco: "))
estC = input("Estado civil (S: soltero, C: casado): ")
vive = input("Si vive en campo o cuidad (U: urbano, R: rural): ")
añoN = (2023-añoN)
if (añoP > 10) and (num >= 2):
  print("APROBADO")
elif (estC == "C") and (num > 3) and (45 < añoN > 55):
  print("APROBADO")
elif (ingr > 2500000) and (estC == "S") and (vive == "U"):
  print("APROBADO")
elif (ingr > 3500000) and (añoP > 5):
  print("APROBADO")
elif (vive == "R") and (estC == "C") and (num < 2):
  print("APROBADO")
else:
  print("RECHAZADO")