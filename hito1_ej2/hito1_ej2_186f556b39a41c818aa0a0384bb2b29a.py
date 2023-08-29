#Contestador de celular
#profesor la condicion que corresponde antes de las 14 horas esta incluida en la condicion de 00:00 y 07:00
#haci que la condicion antes de las 14 horas le agregue que tambien fuera mayor a las 7 
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