#Contestador de celular
telefono = str(input("ingrese un numero telefonico:"))
hora =  int(input("ingrese hora de la llamada:"))
if hora >= 0 and hora <= 7:
  print("contestar")
elif hora > 7 and hora <= 14:
  if telefono%10**3 == 909:
    print ("contestar")
  else: 
    print("no contestar") 
elif hora >= 17 and hora <= 19:
  if telefono%10**3 == 877:
    print("contestar")
  else:
    print("no contestar")
elif hora >= 19 and hora <= 23:
  print("no contestar")
else:
  print("no contestar")    