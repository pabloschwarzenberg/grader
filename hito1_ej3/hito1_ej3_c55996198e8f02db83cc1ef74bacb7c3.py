#Aprobación de créditos
#Nombre del creador: Daniel Ugarte
numeroingresos = int(input("ingrese su numero de ingresos: "))
nacimiento = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese su numero de hijos: "))
añospertenecia = int(input("ingrese sus años de pertenencia al banco: "))
estadocivil = str(input("ingrese si esta Casado(C) o Soltero(S): "))
localidad = str(input("ingrese si vive en Ciudad(U) o Campo(R): "))
añoactual = 2021
Edad = añoactual - nacimiento
if añospertenecia > 10 and hijos >= 2:
  print("APROBADO")
elif str(estadocivil) == "C" and hijos > 3 and Edad > 45 and Edad <= 55:
  print("APROBADO")
elif numeroingresos > 2500000 and str(estado_civil) == "S" and str(localidad) == "U":
  print("APROBADO")
elif numeroingresos > 3500000 and anos_pertenecia > 5 :
  print("APROBADO")
elif str(localidad) == "R" and str(estadocivil) == "C" and hijos < 2 :
  print("APROBADO")
else:
  print("RECHAZADO")      