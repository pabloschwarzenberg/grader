#Aprobación de créditos
Ingreso = int(input("Ingreso (en pesos) "))
birth = int(input("Año de nacimiento "))
Age = 2018 - birth
n_hijos = int(input("Número de hijos "))
loyalty = int(input("Años de pertenencia al banco "))
forever_alone = str(input("Estado civil "))
pc_console = str(input("urbano o rural (U o R) "))
if loyalty > 10 and n_hijos >= 2:
  print("APROBADO")
elif forever_alone == "C" and n_hijos > 3 and 45 < Age < 55:
  print("APROBADO")
elif Ingreso > 2500000 and forever_alone == "S" and pc_or_console == "U":
  print("APROBADO")
elif Ingreso > 3500000 and loyalty > 5:
  print("APROBADO")
elif pc_console == "R" and forever_alone == "C" and n_hijos >=2:
  print("APROBADO")
elif pc_console == "R" and forever_alone == "C" and n_hijos <=2:
  print("APROBADO")
else:
  print("RECHAZADO")