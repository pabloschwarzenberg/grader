#Contestador de celular
fono= (input("Ingrese numero de telefono(RECUERDE QUE SON 8 DIGITOS): "))
hora= int(input("Ingrese hora de atencion: "))

ultn= fono[-3:]
prin= fono[:3]

if hora > 0 and hora <= 7:
  print("Contestar")
elif hora > 7 and hora < 14:
  if ultn == "909":
      print("Contestar")
  else:
      print("No contestar")
elif hora > 17 and hora < 19:
   if prin == "877":
        print ("No contestar")
   else:
        print ("Contestar")
elif hora > 19:
    print("No contestar")