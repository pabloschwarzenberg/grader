#Contestador de celular
from math import floor
telefono = float(input("ingrese su numero de telefono de 8 digitos "))
hora=float(input("ingrese la hora de la llamada con dos digitos "))
primerdigito = floor(telefono/10**7)
segundodigito = floor((telefono % 10**7)/10**6)
tercerdigito = floor((telefono % 10**6)/10**5)
cuartodigito = floor((telefono % 10**5)/10**4)
quintodigito = floor((telefono % 10**4)/10**3)
sextodigito = floor((telefono % 10**3)/10**2)
septimodigito = floor((telefono % 10**2)/10**1)
octavodigito = floor((telefono % 10**1)/10**0)
if (telefono > 99999999 or telefono < 10000000):
  print("ingrese un numero de telefono de 8 digitos que no empiece con 0")
else:
  if hora<=7 and hora>=0:
   print ("contestar")
  if hora>7 and hora<14 and sextodigito==9 and septimodigito==0 and octavodigito==9:
     print("contestar")
  else:   
     if hora>7 and hora<14:
      print("no contestar")
  if hora>=17 and hora<=19 and primerdigito==8 and segundodigito==7 and tercerdigito==7:
     print("no contestar")
  else: 
     if hora>=17 and hora<=19:
      print("contestar")
  if hora>19 and hora<24:
     print("no contestar")    
  if hora>=14 and hora<17:
     print("no contestar")