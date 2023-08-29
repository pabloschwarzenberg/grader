num = str(input("Ingresa numero telefonico: "))
hr = int(input("Ingresa la hora de la llamada: "))
m = num[5:9]
n = num[0:3]
int(n)
int(m)
if (hr >= 0) and (hr <=19):
  if (hr >= 0) and (hr <= 7):
      print("CONTESTAR")
if(hr >= 7) and (hr <= 14):
        if (m == "909"):
          print("CONTESTAR")
else:
      print("NO CONTESTAR")
  
if(hr >= 17) and (hr <= 19):
         if (n == "877"):
          print("NO CONTESTAR")
else:
  print("CONTESTAR")

  