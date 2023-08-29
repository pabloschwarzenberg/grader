# Aprobación de créditos
Ingreso = int(input("Indique su ingreso en pesos: "))
Anio_nacimiento = int(input("Indique su año de nacimiento: "))
Num_hijos = int(input("Indique número de hijos: "))
Anios_pert_banco = int(input("Indique años de pertenencia al banco: "))
Estado_civil = input('Indique su estado civil: ("S": soltero, "C", casado)')
Vivienda = input('Indique si vive en campo o en ciudad: ("U": urbano, "R": rural)')
# Calculo 1
# Año actual es 2023
Edad = 2023 - Anio_nacimiento
# Calculo
if Anios_pert_banco > 10 and Num_hijos >= 2:
      print("APROBADO")
elif Estado_civil == 'C' and Num_hijos > 3 and (45 <= Edad <= 55):
      print("APROBADO")
elif Ingreso > 2500000 and Estado_civil == "S" and Vivienda == "U":
      print("APROBADO")
elif Ingreso > 3500000 and Anios_pert_banco > 5:
      print("APROBADO")
elif Vivienda == "R" and Estado_civil == "C" and Num_hijos < 2:
      print("APROBADO")
else:
      print("RECHAZADO")