#Aprobación de créditos
ingreso= int(input("Ingresos: "))
mira= int(input("Año de nacimiento: "))
hijos= int(input("Cantidad de hijos: "))
pertenencia= int(input("años en el banco: "))
estadocivil= str(input("Estado civil, S-Soltero, C-Casado: "))
domicilio= str(input("Donde vive, U-Urbano, R-Rural: "))
ano= 2022-mira

if ingreso >= 10 and hijos >= 2:
  print("APROBADO")

if estadocivil == "C" and hijos >= 3 and ano >= 45:
  print("APROBADO")

if ingreso >= 2500000 and estadocivil == "S" and domicilio == "R":
  print("APROBADO")

if ingreso >= 3500000 and pretenencia >= 5:
  print("APROBADO")

if domicilio == "U" and estadocivil == "C" and hijos >= 2:
  print("APROBADO")

else:
  print("APROBADO")