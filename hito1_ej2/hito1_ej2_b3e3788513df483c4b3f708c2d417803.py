#Contestador de celular
numTelefonico = int(input("ingresar número telefónico: "))
horaLlamada = int(input("ingresar hora de la llamada: "))

if horaLlamada >= 0 and horaLlamada < 7:
   print("CONTESTAR")
elif horaLlamada >= 7 and horaLlamada < 14:
   if numTelefonico % 100 == 9:
       print("CONTESTAR")
   else:
     print("NO CONTESTAR")
elif horaLlamada >= 14 and horaLlamada < 17:
  print("NO CONTESTAR")
elif horaLlamada >= 17 and horaLlamada < 19:
   if numTelefonico // 10000000 == 877:
      print("CONTESTAR")
   else:
     print("NO CONTESTAR")
else:
  print("NO CONTESTAR")
      