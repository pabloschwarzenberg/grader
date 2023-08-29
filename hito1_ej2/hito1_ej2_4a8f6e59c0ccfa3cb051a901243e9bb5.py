#Contestador de celular
numero_telefono = str(input("numero de telefono que esta llamando: "))
hora = int(input("La hora cuando se llamo: "))

NT = numero_telefono[0:3]
HR = numero_telefono[5:8]

if 0 <= hora <= 7:
  print("CONTESTAR")

elif 7< hora <= 14:
  if HR == "909":
    print("CONTESTAR")
    
  else:
    print("NO CONTESTAR")

elif 17 <= hora <= 19:
  if NT == "877":
    print("nNO CONTESTAR")
    
  else:
    print("CONTESTAR")

else: 
  print("NO CONTESTAR")