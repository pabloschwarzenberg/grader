#Contestador de celular
fono= int(input("ingrese telefono "))
hora=int(input("ingrese hora "))
term909=int(fono%1000)
com877=int(fono//100000)
if(fono>99999999)and(fono<10000000):
  print("telefono fuera de rango")
elif(hora<=0)and(hora>=23):
  print("hora fuera de rango")
elif(hora>=0)and(hora<=7):
  print("CONTESTAR")
elif(hora<14)and(hora>7):
  if term909==909:
      print("CONTESTAR")
  else:
      print("NO CONTESTAR")
elif(hora<=19)and(hora>=17):
  if com877==877:
      print("NO CONTESTAR")
  else:
      print("CONTESTAR")
elif(hora>19):
  print("NO CONTESTAR")