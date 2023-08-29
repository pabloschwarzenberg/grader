#Contestador de celular

celular=int(input("ingrese celular: "))
hora=int(input("ingrese hora llamada:"))

if hora>=0 and hora<=7:
  print("CONTESTAR")

elif hora>=14 and hora <17 or str(celular)[5:] == "909":
  print("CONTESTAR")

elif hora>=17 and hora <=19 and str(celular)[0:3] !="877":
  print("CONTESTAR")

else:
  print("NO CONTESTAR")