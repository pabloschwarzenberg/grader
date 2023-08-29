#Contestador de celular
Num=int(input("Ingresa numero telefonico:"))
Hora=int(input("Ingrese hora de la llamada:"))
if((Num//10000000)>10):
  print("NO CONTESTAR")
elif((Hora>23) or (Hora<0)):
  print("NO CONTESTAR")
elif ((Num//10000000)<10) and (0<Hora<23):
  if(0<Hora<7):
    print("CONTESTAR")
  elif(7<Hora<14) and ((Num-(Num-909))!=909):
    print("NO CONTESTAR")
  elif(7<Hora<14) and ((Num-(Num-909))==909):
    print("CONTESTAR")
  elif(14<Hora<17):
    print("NO CONTESTAR")
  elif(17<Hora<19) and ((Num-(Num-87700000))!=87700000):
    print("CONTESTAR")
  elif(17<Hora<19) and ((Num-(Num-87700000))==87700000):
    print("NO CONTESTAR")
  elif(19<Hora<23):
    print("NO CONTESTAR")