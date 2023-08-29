#Contestador de celular

numero_telefonico = int(input("Ingrese un numero de 8 digitos: "))
hora = int(input("Ingrese una hora entre 0 y 23: "))


str_numero_telefonico = str(numero_telefonico)
#Ejemplos de numeros:
# 78735653
# 01234567

if hora >= 00 and hora <= 7:
  print("EMERGENCIA!")

if hora >= 8 and hora <=14: 
  if str_numero_telefonico[5:8] == "909":
    print("CONTESTAR")
  elif str_numero_telefonico != "909":
    print("NO CONTESTAR")

#Revisar de aqui para abajo:)
if str_numero_telefonico[0:3] == "877" and hora >=17 and hora <= 19: 
  print("No Contestar")
elif str_numero_telefonico[0:3] != "877" or hora >= 17 and hora <= 19:
  print("Contestar")

if hora > 19:
  print("No contestar")