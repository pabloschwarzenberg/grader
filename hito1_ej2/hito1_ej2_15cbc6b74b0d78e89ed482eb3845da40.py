#Contestador de celular
y = int(input("ingrese numero de telefono:"))
x = int(input("ingrese hora de llamada:"))

if x:
  if (x >= 0) and (x <= 7) :
    print("contestar")
  elif x:
   if (x >= 7) and (x <= 14) and (y %1000 == 909):
     print("contestar")
   else:
     print("no contestar")
  elif x:
   if x >= 17 and x <= 19 or y //1000 == 877:
    print("contestar")
   else:
      print("no contestar")
  else:
    x >= 20 and x <= 24
    print("no contestar")