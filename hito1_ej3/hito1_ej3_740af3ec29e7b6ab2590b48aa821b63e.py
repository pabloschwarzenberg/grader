#Aprobación de créditos
ingreso = int(input("Ingresos en pesos: "))
Año_de_nacimiento = int(input("Año de nacimiento: "))
Numero_de_hijos = int(input("Cantidad de hijos: "))
Años_de_pertenecia_al_banco = int(input("Años que pertenece al banco: "))
Estado_civil = input("Estado civil S/C (Soltero/Casado): ")
Vivienda = input("Lugar de vivienda U/R (Urbano/Rural): ")
Años = 2021 - Año_de_nacimiento
if Años_de_pertenecia_al_banco > 10 and Numero_de_hijos >= 2:
  print("APROBADO")
elif Estado_civil == "C" and Numero_de_hijos > 3 and Años >= 45 and Años <= 55:
  print("APROBADO")
elif ingreso > 2500000 and Estado_civil == "S" and Vivienda == "U":
  print("APROBADO")
elif ingreso > 3500000 and Años_de_pertenecia_al_banco > 5:
  print("APROBADO")
elif Vivienda == "R" and Estado_civil == "C" and Numero_de_hijos <2: 
  print("APROBADO")
else:
  print("RECHAZADO")