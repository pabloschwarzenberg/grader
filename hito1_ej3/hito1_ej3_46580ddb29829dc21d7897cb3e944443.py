#Aprobación de créditos
ingresos = int(input("Ingrese sus ingresos en pesos: "))
nacimiento = int(input("Ingrese su ano de nacimiento: "))
nhijos = int(input("Ingrese su numero de hijos: "))
pertenencia = int(input("Ingrese cantidad de anos en el banco: "))
Estadocivil = input("Ingrese su estado civil, Soltero'S' o Casado'C': ")
vive = input("Ingrese una 'U' si vive en zona urbana o 'R' si vive en zona rural: ")

nacimiento =  2022 - nacimiento
if pertenencia >= 10 and nhijos >= 2:
  print("APROBADO")
elif Estadocivil=="C" and nhijos >3 and nacimiento > 45 and nacimiento < 55:
  print("APROBADO")
elif ingresos > 2500000 and Estadocivil == "S" and vive =="U":
  print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5:
  print("APROBADO")
elif vive=="R" and Estadocivil=="C" and nhijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")