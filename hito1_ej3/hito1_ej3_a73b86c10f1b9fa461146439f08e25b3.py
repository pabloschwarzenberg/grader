#Aprobación de créditos
      
ingreso = int(input("Ingrese sus ingresos:$ "))
nacimiento = int(input("Inngrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
p_banco = int(input("Años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil, si esta soltero escriba ""S"" o si esta casado responda con ""C"": ")
ubicacion = input("Si usted vive en zona urbana o ciudad responda ""U"" o si vivie en zona rural o campo responda ""R"": ")
fecha = 2022
edad = fecha - nacimiento
if (p_banco > 10) and (hijos >= 2):
  print("APROBADO")
  
elif (estado_civil == "C" or estado_civil == "c") and (hijos > 3) and (edad > 45 and edad < 55):
  print("APROBADO")
      
elif (ingreso > 2500000) and (estado_civil == "S" or estado_civil == "s") and (ubicacion == "U" or ubicacion == "u"):
  print("APROBADO")  
    
elif (ingreso > 3500000) and (p_banco > 5):
  print("APROBADO")
  
elif (ubicacion == "R" or ubicacion == "r") and (estado_civil == "C" or estado_civil == "c") and (hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")