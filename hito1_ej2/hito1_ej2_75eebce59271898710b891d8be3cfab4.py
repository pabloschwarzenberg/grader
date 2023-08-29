#Contestador de celular
num = str(input("Ingresar su numero de telefono: "))
hr = int(input("Ingresar la hora de la llamada: "))
m = num[5:9]
n = num[0:3]
int(n)
int(m)
if (hr >= 0) and (hr <= 19):
  if (hr >=0) and (hr<= 7):
     print("Contestar")
  elif (hr >= 7) and (hr <= 14):
    if (m == "909"):
     print("Contestar")
    else:
     print("No contestar")
  elif (hr >= 17) and (hr <= 19):
     if (n == "877"):
       print("No contestar")
     else:
      print("Contestar")
  else:
     print("No contestar")
else:
    print("No contestar")