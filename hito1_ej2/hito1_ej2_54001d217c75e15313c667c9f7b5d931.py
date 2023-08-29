#Contestador de celular
numero = int(input("Ingrese numero: ")) #77389909
hora = int(input("Ingrese hora: ")) #13

numero = str(numero)

if hora >= 0 and hora <= 7:
  print("CONTESTAR")
elif hora < 14 and numero [-3:] == "909":
  print("CONTESTAR")
elif hora >= 17 and hora <= 19 and not numero [0:3] == "877":
  print("CONTESTAR")
else:
  print("NO CONTESTAR")  