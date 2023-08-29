#Patricio
#Contestador de celular
numero = int(input("Numero: "))
hora = int(input("Hora: "))
caso1a = str(numero)
caso1b = (caso1a[5:8])
caso1c = str(909)
caso2a = str(numero)
caso2b = (caso2a[0:3])
caso2c = str(877)
if hora >=0 and hora <= 7:
  print ("CONTESTAR")
if hora > 7 and hora <= 14:
  if caso1b == caso1c:
    print ("CONTESTAR")
  else:
    print ("NO CONTESTAR")
if hora > 14 and hora < 17:
  print ("NO CONTESTAR")
if hora >=17 and hora <=19:
  if caso2b == caso2c:
    print ("NO CONTESTAR")
  else:
    print ("CONTESTAR")
if hora > 19:
  print ("NO CONTESTAR") 