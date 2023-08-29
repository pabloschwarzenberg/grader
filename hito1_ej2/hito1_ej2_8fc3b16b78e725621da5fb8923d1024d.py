#Contestador de celular
num = str(input("Ingresa numero telefonico: "))
hr = int(input("Ingresa hora de la llamada: "))
x = num[5:9]
z = num[0:3]
int(z)
int(x)
if (hr >= 0) and (hr <=19):
  if (hr >= 0) and (hr <= 7):
      print("CONTESTAR")
if(hr >= 7) and (hr <= 14):
        if (x == "909"):
          print("CONTESTAR")
else:
      print("NO CONTESTAR")
    