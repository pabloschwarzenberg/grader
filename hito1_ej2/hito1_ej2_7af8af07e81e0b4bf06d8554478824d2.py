llamada=(input("Ingrese numero telefonico (8 cifras) "))
hora=int(input("Ingrese hora de la llamada (0 a 23) "))

FiltroLlamadas1=llamada[-3:]
FiltroLlamadas2=llamada[:3]


if(0<=hora<=7):
  print("CONTESTAR")
elif(hora>=19):
  print("NO CONTESTAR")
elif(7<hora<14):
  if(FiltroLlamadas1=="909"):
   print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif(17<=hora<=19):
  if(FiltroLlamadas2=="877"):
   print("NO CONTESTAR")
  else:
    print("CONTESTAR")