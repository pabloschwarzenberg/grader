#Aprobación de créditos
numero_ingresos = int(input("ingrese su numero de ingresos: "))
nacimiento = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese su numero de hijos: ")) 
anos_pertenecia = int(input("ingrese sus años de pertenencia al banco: "))
estado_civil = str(input("ingrese si esta Casado(C) o Soltero(S): "))
localidad = str(input("ingrese si vive en Ciudad(U) o Campo(R): "))
ano_actual = 2021
Edad = ano_actual - nacimiento
if anos_pertenecia > 10 and hijos >= 2: 
  print("APROBADO")  
elif str(estado_civil) == "C" and hijos > 3 and Edad > 45 and Edad <= 55: 
  print("APROBADO") 
elif numero_ingresos > 2500000 and str(estado_civil) == "S" and str(localidad) == "U":
  print("APROBADO")
elif numero_ingresos > 3500000 and anos_pertenecia > 5 :
  print("APROBADO")   
elif str(localidad) == "R" and str(estado_civil) == "C" and hijos < 2 :
  print("APROBADO")
else:
  print("RECHAZADO")      