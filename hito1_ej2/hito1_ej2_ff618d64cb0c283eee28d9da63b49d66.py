#Contestador de celular
a=int(input("ingrese numero telefonico"))
b=int(input("ingrese hora de la llamada"))

if(b>19):
  print("NO CONTESTAR")

if(0<b<7):
  print("CONSTESTAR")

if(7<b<14):
  if(a%1000==909):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")

if(14<b<17):
  print("NO CONTESTAR")
    
if(17<b<19):
  print("CONTESTAR")
  if(a==87765545):
    print("NO CONTESTAR")    