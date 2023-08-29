#Aprobación de créditos
ingreso = int(input("ingreso: "))
año_de_nacimiento = int(input("año de nacimiento: "))
numero_de_hijos = int(input("numero de hijos: "))
años_de_pertenencia_al_banco = int(input("años de pertenencia al banco: "))
estado_civil = str(input("estado civil (casado: C, soltero: S): "))
vives_en_campo_o_ciudad = str(input("vives en campo o ciudad(campo: R, ciudad: U): "))

if (años_de_pertenencia_al_banco > 10 and numero_de_hijos >= 2):
  print("APROBADO")
  
elif (estado_civil== "C" and numero_de_hijos > 3 and 55 > 2021 - año_de_nacimiento > 45):
  print("APROBADO")
  
elif (ingreso > 3500000 and estado_civil== "S" and vives_en_campo_o_ciudad== "U"):
  print("APROBADO")
  
elif (ingreso > 2500000 and años_de_pertenencia_al_banco > 5):
  print("APROBADO")
  
elif (vives_en_campo_o_ciudad== "R" and estado_civil== "C" and numero_de_hijos < 2):
  print("APROBADO")

else:
  print("RECHAZADO")