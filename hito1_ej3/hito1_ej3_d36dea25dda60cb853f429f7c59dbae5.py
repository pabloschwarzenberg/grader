#Aprobación de créditos
cliente = []

ingresos = int(input("Indique sus ingresos: "))
cliente.append(ingresos)#
nacimiento = int(input("Indique su ano de nacimiento: "))
nacimiento = 2023 - nacimiento
cliente.append(nacimiento)#
hijos = int(input("Indique su nro de hijos: "))
cliente.append(hijos)#
banco = int(input("Indique sus anos de pertenencia al banco: "))
cliente.append(banco)#
civil = input("Indique sus estado civil: ")
cliente.append(civil)#
vive = input("Indique si vive en campo o ciudad: ")
cliente.append(vive)#
if cliente[3] >= 10 and cliente[2] >= 2:
  print("APROBADO")
if cliente[4] == "C" and 45 <= cliente[1] <= 55 and cliente[2] > 3:
  print("APROBADO")
if cliente[0] >= 2500000 and cliente[4]=="S" and cliente[5]=="U":
  print("APROBADO")
if cliente[0] >= 3500000 and cliente[3] > 5:
  print("APROBADO")
if cliente[5] == "R" and cliente[2] < 2:
  print("APROBADO")
else: 
  print("RECHAZADO")