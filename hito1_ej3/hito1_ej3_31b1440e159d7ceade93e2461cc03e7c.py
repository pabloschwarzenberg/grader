Ingreso = eval(input("Ingreso (pesos): "))
Nacimiento = eval(input("Año de nacimiento: "))
Hijos = eval(input("Numero de hijos: "))
AñosB = eval(input("Años de pertenencia en el banco: "))
Estado = input("Estado Civil (S, soltero C,Casado): ")
Lugar = input("Sector de residencia (U, urbano R, rural: ")

Edad = 2020 - Nacimiento

if AñosB > 10 and Hijos >= 2:
  print("APROBADO")
if Estado == "C" and Hijos > 3 and 45<Edad<55:
  print("APROBADO")
if Ingreso > 2500000 and Estado == "S" and Lugar == "R":
  print("APROBADO")
if Ingreso > 3500000 and AñosB > 5:
  print("APROBADO")
if Lugar == "R" and Estado == "C" and Hijos < 2:
  print("APROBADO")
else:
  print("REPROBADO")