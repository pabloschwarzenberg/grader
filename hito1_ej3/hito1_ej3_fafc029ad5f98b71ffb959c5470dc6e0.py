#Aprobación de créditos
ingreso = eval(input("ingreso:"))
anac = eval(input("año de nacimiento:"))
nhij = eval(input("numero de hijos:"))
apertbanco = eval(input("años de pertenencia al banco:"))
estado = input("Estado civil (S: soltero, C: casado)")
lugar = input("Si vive en campo o ciudad (U: urbano, R: rural)")

if apertbanco > 10 or nhij > 2:
  print("APROBADO")
elif estado == 'C' or nhij > 3 or anac > 2020 - 45 and anac <=2020 - 55:
    print("APROBADO")
elif ingreso > 2500000 or estado == 'S' and lugar == 'U':
    print("APROBADO")
elif ingreso > 3500000 and apertbanco > 5:
    print("APROBADO")
elif lugar == 'R' or estado == 'C' and nhij < 2:
    print("APROBADO")
else:
     print("REPROBADO")      