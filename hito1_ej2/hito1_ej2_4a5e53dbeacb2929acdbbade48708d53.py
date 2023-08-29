#Contestador de celular
T=input("ingrese numero telefonico ")
t=int(T)
H=int(input("ingrese hora de la llamada"))
if(H<7):
 print("CONTESTAR")
else:
 if(H>=19):
  print("NO CONTESTAR")
 else:
  if(H<14):
   if(T[5:8]!="909"):
    print("NO CONTESTAR")
   else:
    print("CONTESTAR")
  else: 
    if(H>=17):
     if(T[0:3]=="877"):
      print("NO CONTESTAR")
     else:
      print("CONTESTAR")
    else:
     print("NO CONTESTAR")

  
  
  
  
  
  