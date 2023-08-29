ingreso = int(input("Ingrese sus actividades:$ "))
ano = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su numero de hijos: "))
ano_en_el_banco = int(input("Años de pertenencia: "))
estado_civil = input("Su estado civil, si esta soltero escriba ""S"" o si esta casado responda con ""C"": ")
vivienda = input("Si usted vive en zona urbana o ciudad responda ""U"" o si vivie en zona rural o campo responda ""R"": ")
ano2 = 2022
edad = ano2 - ano
if (ano_en_el_banco > 10) and (hijos >= 2):
  print("APROBADO")
  
elif (estado_civil == "C" or estado_civil == "c") and (hijos > 3) and (edad > 45 and edad < 55):
  print("APROBADO")
      
elif (ingreso > 2500000) and (estado_civil == "S" or estado_civil == "s") and (vivienda == "U" or vivienda == "u"):
  print("APROBADO")  
    
elif (ingreso > 3500000) and (ano_en_el_banco > 5):
  print("APROBADO")
  
elif (vivienda == "R" or vivienda == "r") and (estado_civil == "C" or estado_civil == "c") and (hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")