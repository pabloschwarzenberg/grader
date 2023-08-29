#Contestador de celular
numero = int(input(">>> Ingrese Numero telefonico : "))
hora = int(input(">>> Ingrese hora de la llamada : "))

if hora >= 0 and hora <= 7:
  print(">>> Resultado : CONTESTAR")

elif hora >7 and hora<=14:
  if str(numero)[-3:] == "909":
    print(">>> Resultado : CONTESTAR")
  else:
    print(">>> Resultado : NO CONTESTAR")
elif hora >14 and hora <= 17:
  print(">>> Resultado : NO CONTESTAR")

elif hora >17 and hora <= 19:
  if str(numero)[:3] == "877":
    print(">>> Resultado : NO CONTESTAR")
  else:
    print(">>> Resultado : CONTESTAR")

else:
  print(">>> Resultado : NO CONTESTAR")      