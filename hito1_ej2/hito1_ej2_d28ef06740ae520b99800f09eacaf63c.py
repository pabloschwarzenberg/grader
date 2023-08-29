#Contestador de celular
tel=int(input("Ingrese numero telefonico:"))
hr=int(input("Ingrese hora de la llamada:"))

if (0<=hr<=7):
  print ("CONTESTAR")
elif hr<=14 and ((tel%1000)==909):
  print ("CONTESTAR")
elif 17<=hr<=19 and ((tel//100000)!=877):
  print ("CONTESTAR")
else:
  print ("NO CONTESTAR")