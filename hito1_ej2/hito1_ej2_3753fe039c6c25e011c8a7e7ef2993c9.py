#Contestador de celular
print("bienvenido al contestador automatico!")
nt=int(input("ingrese su numero de 8 cifras porfavor: "))
h=int(input("ingrese la hora de su llamada entre 0 y 23: "))
if(0<=h<=7):
  print("CONTESTAR")
if(8<=h<=14 and nt%1000==909):
  print("CONTESTAR")
if(8<=h<=14 and nt%1000!=909):
  print("NO CONTESTAR")
if(17<=h<=19 and nt//100000!=877):
  print("CONTESTAR")
if(17<=h<=19 and nt//100000==877):
  print("NO CONTESTAR")
if(h>19):
  print("NO CONTESTAR")