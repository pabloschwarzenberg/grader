numero=int(input("ingrese el numero:"))
hora=int(input("infrese la hora:"))
if(00<=hora<7):
  print("contestar")
elif(hora>19):
  print("no contestar")
elif(7<hora<14) :
  if(numero%1000==909):
    print("contestar")
  else:
   print("no contestar")

elif(17<=hora<=19):
  if(numero//100000==877):
    print("no contestar")
  else:
   print("contestar")