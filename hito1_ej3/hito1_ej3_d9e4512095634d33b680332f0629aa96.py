#Aprobación de créditos
print("INGRESE LOS SIGUIENTES DATOS")

ing = int(input("Ingreso (en pesos): ")) 
nac = int(input("Año de nacimiento: ")) 
num_hijos = int(input("Número de hijos: "))
años = int(input("Años de pertenencia al banco: ")) 
es_civil = str(input("Estado civil (""S"" para soltero, ""C""para casado: "))  
vive = str(input("¿Vive en campo o cuidad? (""U"" para urbano, ""R"" para rural):")) 

nac_años = 2022 - nac


if años >= 10 and num_hijos >= 2:
  print("APROBADO")

elif es_civil == "C" and num_hijos >= 3 and 55 >= nac_años >= 45:
  print("APROBADO")    

elif ing >= 2500000 and es_civil == "S" and vive == "R":
  print("APROBADO")  

elif ing >= 3500000 and años >= 5:
  print("APROBADO")

elif vive == "U" and es_civil == "C" and num_hijos <= 2: 
  print("APROBADO")

else:
  print("NO APROBADO")      