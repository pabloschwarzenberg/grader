#Aprobación de créditos
dinero = eval(input("sus ingresos en pesos: "))
nacimiento = eval(input("su año de nacimiento: "))
hijos = eval(input("su numero de hijos: "))
años_banco = eval(input("sus años de pertenencia al banco: "))
estado_civil = input("usted es soltero o casado: ")
lugar = input("vive en campo o ciudad: ")

if (años_banco > 10) and (hijos >= 2):
  print("APROBADO")
elif (estado_civil == "C") and (hijos >= 3) and ( 45 <= nacimiento >= 55):
  print("APROBADO")
elif (dinero > 2500000) and (estado_civil == S) and (lugar == "C"):
  print("APROBADO")
elif (dinero > 3500000) and (años_banco > 5):
  print("APROBADO")
elif (lugar == "R") and (estado_civil == "C") and (hijos < 2):
  print("APROBADO")
else:
  print("RECHAZADO")