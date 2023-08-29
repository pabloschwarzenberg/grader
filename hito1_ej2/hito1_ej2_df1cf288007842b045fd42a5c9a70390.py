#Contestador de celular
telefono = int(input())
hora = int(input())

if hora >= 0 and hora <= 7:
  print("CONTESTAR")
  
elif hora < 14 and str(telefono)[5:8] == "909":
  print("CONTESTAR")
     
elif (hora >= 17 and hora <= 19) and str(telefono)[0:3] != "877":
  print("CONTESTAR")
  
else:
  print("NO CONTESTAR")