telefono=int(input("igrese numero telefonico "))
hora=int(input("ingrese hora de la llamada "))
telefono1=str(telefono)[-3:]
telefono2=str(telefono)[0:3]
if(hora>0 and hora<7):
  print("CONTESTAR")
elif(hora>7 and hora<=14 and telefono1=="909"):
  print("CONTESTAR")
elif(hora>7 and hora<=14):
  print("NO CONTESTAR")
elif(hora>14 and hora<=17):
  print("NO CONTESTAR ")
elif(hora>17 and hora<=19 and telefono2=="877"):
  print("NO CONTESTAR")
elif(hora>17 and hora<=19):
  print("CONTESTAR")
elif(hora>19):
  print("NO CONTESTAR")
  

  
      