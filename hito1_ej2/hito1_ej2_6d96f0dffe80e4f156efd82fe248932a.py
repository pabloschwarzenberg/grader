#Contestador de celular
celular = int(input("Ingrese su numero: "))
hora = float(input("Ingrese hora de la llamada: "))
resto = celular % 1000
celular = int(celular/1000)
print("3 ultimos digitos",resto)
inicio = celular//100
print("3 primeros digitos",inicio)
if 0<=hora<=7:
 print("CONTESTAR")
else:
 if hora<=8<=14:
  print("NO CONTESTAR")
 else:
  if resto==909:
   print("CONTESTAR")
  else:
   if hora>=17<=19:
    print("NO CONTESTAR")
   else:
    if inicio==877:
     print("NO CONTESTAR")
    else:
     if hora>19:
      print("NO CONTESTAR")