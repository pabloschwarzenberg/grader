#Contestador de celular
n=int(input("Ingresa el numero de teléfono: "))
h=int(input("Ingresa la hora: "))
if h>=00 and h<=7:
  print("CONTESTAR")
elif h<14 and h>7 and n%1000==909:
  print("CONTESTAR")
elif h<14 and h>7 and n%1000!=909:
  print("NO CONTESTAR")

elif h>=17 and h<=19 and n%100000==877:
  print ("CONTESTAR")
elif h>=17 and h<=19 and n%100000!=877:
  print ("NO CONTESTAR")
elif h>19:
  print("NO CONTESTAR")

  
  