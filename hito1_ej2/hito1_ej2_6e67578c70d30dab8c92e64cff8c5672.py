Telefono = input("ingresa número telefónico: ")
longitud = len(Telefono)
if longitud == 8:
  print ("número correcto")
else:
   print("CONTESTAR")
Horario = int(input("Señalar hora: "))
if Horario > 0 and Horario <= 7:
  print("CONTESTAR")
if Horario >= 7 and Horario <= 14:
  if Telefono[5:8]!='909':
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if Horario > 14 and Horario <= 17:
  print("NO CONTESTAR")
if Horario >17 and Horario <=19:
  if Telefono[0:3]!='877':
    print("CONTESTAR")
  else: 
    print("NO CONTESTAR")
if Horario >= 19 and Horario <= 23:
 print("NO CONTESTAR")