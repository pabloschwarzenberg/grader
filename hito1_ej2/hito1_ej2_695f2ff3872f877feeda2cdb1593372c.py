N=int(input("Ingrese numero telefonico"))
H=int(input("Ingrese hora de la llamada"))
     
if(0<H<7):
  print("CONTESTAR")
  
if(7<H<14):
  if((N%1000)==909):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
  
if(17<H<19):
   if((N//100000)==877):
     print("NO CONTESTAR")
   else:
     print("CONTESTAR")
 
if(19<H<23):
    print("NO CONTESTAR")
  