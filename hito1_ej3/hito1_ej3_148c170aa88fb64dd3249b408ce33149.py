#atención automática de Banco
ingreso=int(input("¿su ingreso mensual cuanto es?:"))
año_nacimiento=int(input("ingrese su año de nacimiento:"))
año_actual=2021-año_nacimiento
hijos=int(input("ingrese numero de hijos:"))
fidelidad=int(input("ingrese años de pertenencia en el banco:"))
estado_civil=input("ingrese S si usted es soltero o ingrese C si usted es casado:")
vivienda=input("ingrese U si vive en un lugar urbano o ingrese R si vide en zona rural:")
if(fidelidad>=10) and (hijos>=2):
  print(",APROBADO")
elif(estado_civil=="C") and (hijos>=3) and (año_actual in range(45,55)):
  print("APROBADO")
elif(ingreso>=2500000) and (estado_civil=="S") and (vivienda=="U"):
  print("APROBADO")
elif(ingreso>=3500000) and (fidelidad>=5):
  print("APROBADO")
elif(vivienda=="R") and (estado_civil=="C") and (hijos<=2):
  print("APROBADO")