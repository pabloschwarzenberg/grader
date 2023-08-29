numero = int(input("Numero llamada entrante:"))
hora = int(input("Hora De la LLamada:"))



if hora >= 0 and hora <= 7:
  print ("Contestar")
elif hora < 14 and int(str(numero)[-3:]) == 909:
  print ("Contestar")
elif hora >= 17 and hora <= 19 and int(str(numero)[:3]) == 877 :
  print("No Contestar")
elif hora >= 17 and hora <= 19:
  print("Contestar")
elif hora > 19 and hora <= 23:
  print ("No Contestar")
else:
  print("No Contestar")      