#Contestador de celular
n = str(input("ingrese numero de telefono: "))
hr = int(input("ingrese hora de llamada: "))
m = n[5:9]
n = n[0:3]
int(m)
int(n)
if (hr >= 0) and (hr <= 19):
  if (hr >= 0) and (hr <= 7):
    print("CONTESTAR")
  elif (hr >= 7) and (hr <= 14):
        if (m == "909"):
         print("CONTESTAR")
        else:
         print("NO CONTESTAR")
  elif (hr >= 17) and (hr <= 19):
         if(n == "877"):
           print("NO CONTESTAR")
         else:
           print("CONTESTAR")
  else:
      print("NO CONTESTAR")
else:
    print("NO CONTESTAR")