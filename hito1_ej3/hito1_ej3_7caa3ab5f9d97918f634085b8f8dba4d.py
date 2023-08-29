Ingreso = int(input("Ingreso (en pesos): "))
Nacimiento = int(input("Año de Nacimiento: "))
Hijos = int(input("Número de hijos: "))
Años = int(input("Años de pertenencia al banco: "))
Estado = str(input("Estado civil (S: soltero, C: casado): "))
Vive = str(input("Si vive en campo o cuidad (U: urbano, R: rural): "))


Edad= 2020 - Nacimiento

if (int(Años)) > 10 and (int(Hijos) )>= 2:
  print ("APROBADO")
elif Edad > 45 < 55 and Estado == "C":
  print ("APROBADO")
elif Ingreso > 2500000 and Estado =="S" and Vive == "U":
  print ("APROBADO")
elif Ingreso > 3500000 and Años > 5:
  print ("APROBADO")
elif  Vive == "U" and Estado == "C" and Hijos < 2:
  print ("APROBADO")
else:
  print("RECHAZADO")