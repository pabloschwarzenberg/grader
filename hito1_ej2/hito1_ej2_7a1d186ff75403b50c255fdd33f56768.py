#Contestador de celular
Telefono = int(input("Escriba un telefono de 8 cifras"))
Hora = int(input("escriba una hora")) 

Telefono = str(Telefono)

if Hora>=0 and Hora<=7:
  print("contestar")
  
elif Hora<14 and Telefono[-3:] =="909":
  print("contestar")
  
elif Hora>=17 and Hora <=19 and Telefono [0:3] != "877":
  print("contestar")
  
elif Hora>19:
  print("no contestar")
else:
  print("no contestar")