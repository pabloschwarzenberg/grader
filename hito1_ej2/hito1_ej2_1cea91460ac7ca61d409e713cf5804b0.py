#Contestador de celular
x=input("Ingrese numero telefonico:")
y=input("Ingrese hora de llamada:")
if(0<=int(y)<=7):
  print("Resultado: CONTESTAR")
else:
  if(int(y)<14):
    if(int(x[5:])==909):
      print("Resultado: CONTESTAR")
    else:
      print("Resultado: NO CONTESTAR")
  else:
    if(17<=int(y)<=19):
      if(int(x[0:3])==877):
        print("Resultado: NO CONTESTAR")
      else:
        print("Resultado: CONTESTAR")
    else:
      print("Resultado: NO CONTESTAR")
      
        
