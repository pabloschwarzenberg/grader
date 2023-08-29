#Contestador de celular

#nt=numero telefonico
#h=hora de la llamada

nt = int(input("Ingrese número: "))
h = int(input("Ingrese hora: "))

nt = str(nt)

if h>=0 and h<=7 :
  print("CONTESTAR")
  
elif h<14 and nt[-3:] == "909":
  print("CONTESTAR")
  
elif h>=17 and h<=19 and nt[0:3] != "877":
  print("CONTESTAR")
  
elif h>19:
  print("NO CONTESTAR")
else:
  print("NO CONTESTAR")