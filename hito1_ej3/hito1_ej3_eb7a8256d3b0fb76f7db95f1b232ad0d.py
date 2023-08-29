I = eval(input("Ingreso(en pesos):"))
AN = eval(input("Año de nacimiento:"))
E = eval(input("Edad:"))
NJ = eval(input("Número de hijos:"))
BP = eval("Años de pertenencia al banco:")
estado = input("Estado civil (S: soltero, C: casado)")
vive = input("Si vive en campo o cuidad (U: urbano, R: rural):")
if BP > 10 and NJ >= 2:
   print("APROBADO")
elif estado == "C" and NJ >= 3 and AN >= 1975 and AN <= 1965:
   print("APROBADO")
elif I > 2500000 and estado == "S" and vive == "U":
   print("APROBADO")
elif I > 3500000 and BP > 5:
   print("APROBADO")
elif vive == "R" and estado == "C" and NJ < 2:
   print("APROBADO")
else:
  print("RECHAZADO")