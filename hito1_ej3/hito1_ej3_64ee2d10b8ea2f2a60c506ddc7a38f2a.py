Ingreso = int(input("Ingresos Mensuales :"))
Nacimiento = int(input("Edad :"))
Hijos = int(input("Numero de hijos :"))
Banco_anos = int(input("Numero de años en el banco :"))
Estado_civil = str(input("S para soltero y C para casado:"))
Urbano = str(input("U para urbano y R para rural :"))
check = []
if (Banco_anos >=10) and (Hijos >= 2):
  check = check.append(1)
elif (Estado_civil == "C") and (Hijos >= 3) and (Nacimiento <= 1977 or Nacimiento >= 1967):
  check = check.append(1)
elif (Ingreso >= 250000) and (Estado_civil == "S") and (Urbano == "U"):
  check = check.append(1)
elif (Ingreso >= 350000) and (Banco_anos >=10):
  check = check.append(1)
elif (Urbano == "R") and (Estado_civil == "C") and (Hijos < 2):
  check = check.append(1)
if check == None : 
  print("APROBADO")
else :
  print("RECHAZADO")