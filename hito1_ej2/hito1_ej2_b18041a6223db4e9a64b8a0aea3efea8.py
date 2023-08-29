#Contestador de celular
numero = int(input("Numero: "))
hora = int(input("Hora: "))
caso1 = numero%1000
caso2 = numero//100000
if hora >= 0 and hora <= 7:
  print ("CONTESTAR")
if hora > 7 and hora <= 14:
  if caso1 == 909:
    print ("CONTESTAR")
  else:
    print ("NO CONTESTAR")
if hora > 14 and hora < 17:
  print ("NO CONTESTAR")
if hora >=17 and hora <=19:
  if caso2 == 877:
    print ("NO CONTESTAR")
  else:
    print ("CONTESTAR")
if hora > 19:
  print ("NO CONTESTAR")