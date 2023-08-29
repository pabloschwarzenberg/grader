#Contestador de celular
n=int(input("ingrese el numero de telefono: "))
h=int(input("ingrese hora de la llamda: "))
if(h>=0 and h<=7):
  print("CONTESTAR")
elif(n%1000==909):
  print("CONTESTAR")
elif((17<=h<=19) and n//100000 != 877):
  print("CONTESTAR")
elif(h>=19):
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")