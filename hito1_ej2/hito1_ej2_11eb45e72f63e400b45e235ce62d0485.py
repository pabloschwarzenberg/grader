fono=int(input("Ingrese su numero de telefono de 8 digitos: "))
anexotermina= fono%1000
anexocomienza= fono//100000
hora=int(input("Ingrese la hora en formato hh: "))
if hora>=00 and hora<=7:
  print ("CONTESTAR") 
elif hora<14 and anexotermina==909:
  print("CONTESTAR")
elif hora>=17 and hora<=19 and anexocomienza!=877:
  print ("CONTESTAR")
elif hora>19:
  print ("NO CONTESTAR")
else:
 print ("NO CONTESTAR")