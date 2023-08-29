telefono = input("ingrese el numero de telefono: ")
hora = input("ingrese la hora de llamada: ")

#Condicion
if hora >= "00" and hora <= "07":
    print("CONTESTAR")
elif hora <="14":
  if telefono[5:8] == "909":
    print("Contestar")
  else:
    print("NO CONTESTAR")
elif hora >="17" and hora <="19":
  if telefono[5:8] == "877":
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora >= "19":
  print("NO CONTESTAR")
