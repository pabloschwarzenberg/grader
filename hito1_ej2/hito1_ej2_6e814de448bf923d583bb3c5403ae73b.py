#Contestador de celular
numero = int(input("Ingrese numero telefonico"))
hora = int(input("Ingrese hora de la llamada"))
if 7>=hora>=0:
  print("CONTESTAR")
elif 14>=hora>7 and ((numero-909)%100)==0:
  print("CONTESTAR")
elif 17>hora>14:
  print("NO CONTESTAR")
elif 19>=hora>=17:
  if numero-87700000>99999 or 0>numero-87700000:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")
else:
  print ("NO CONTESTAR")



