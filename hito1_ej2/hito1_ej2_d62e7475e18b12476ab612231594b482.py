#Contestador de celular
telefono = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
resto = telefono % 1000 
if hora >= 0 and hora <= 7:
  print("CONTESTAR")  
else:
  if hora <= 14 and resto == 909:
    print("CONTESTAR")
  else: 
    if hora >= 17 and hora <= 19:
      print("NO CONTESTAR")
    elif resto == 877:
      print("CONTESTAR")
    else:
      if hora > 19:
        print("NO CONTESTAR")
    