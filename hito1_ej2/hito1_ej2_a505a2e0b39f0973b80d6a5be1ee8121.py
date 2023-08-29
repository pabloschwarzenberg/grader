#Contestador de celular
NT=int(input("Ingrese el número de teléfono: "))
H=int(input("Ingrese la hora de la llamada: "))
if NT<=99999999 and 0<=H<=23:
  if 0<=H<=7: print("CONTESTAR, POSIBLE EMERGENCIA")
  if H<14 and NT%1000==909: print("CONTESTAR")
  elif H<14: print("NO CONTESTAR")
  else: 
   if H>19: print("NO CONTESTAR")
   if 17<=H<=19 and NT//100000==877: print("NO CONTESTAR")
   elif 17<=H<=19: print("CONTESTAR")
      