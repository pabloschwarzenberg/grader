n=int(input("Ingrese numero telefonico:"))
h=int(input("Ingrese hora de la llamada:"))
if(0<h<7):
  print("CONTESTAR")
else:
  if(7<h<14):
    if(n-((n//1000)*1000)==909):
      print("CONTESTAR")
    else:
      print("NO CONTESTAR")
  else:
    if(17<h<19):
      if(n-(n//1000)>=876):
        print("NO CONTESTAR")
      else:
        print("CONTESTAR")
    else:
      if(h>19):
        print("NO CONTESTAR")