#Contestador de celular
n=int(input("ingrese numero telefonico:"))
h=int(input("ingrese hora de llamada:"))
if(0<=h<=7):
  print("contestar")
if(7<h<14 and n%1000==909):
  print("contestar")
if(7<h<14 and n%1000!=909):
  print("no contestar")
if(17<h<19 and n//100000 !=877):
  print("contestar")
if(17<h<19 and n//100000==877):
  print("no contestar")
if(14<h<17):
  print("no contestar")
if(19<h<24):
 print("no contestar")