#Contestador de celular
num=int(input("¿Quién llama? "))
tim=int(input("¿Qué hora es? "))
if(0<=tim<=7):
  print("CONTESTAR")
if(7<tim<=14):
  if(num%1000==909):
    print("CONTESTAR")
  else:
    prnt("NO CONTESTAR")
if(17<=tim<=19):
  if(num//100000==877):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if((14<tim<17)or(19<tim<=23)):
  print("NO CONTESTAR")
