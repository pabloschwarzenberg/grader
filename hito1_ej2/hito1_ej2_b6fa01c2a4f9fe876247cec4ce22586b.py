tel = input("Ingrese numero telefonico: ")
hr = int(input("ingrese hora de la llamada: "))

if(len(tel) < 8 or len(tel) > 8):
  print("ingrese un numero valido")

elif(hr > 23):
  print("ingrese un hora valida")

elif(hr >= 0 and hr <= 7):
  print("CONTESTAR")

elif(hr < 14  or tel[len(tel)-3] == "909"):
  print("CONTESTAR")

elif(hr >= 17  and hr <= 19 and tel[0:3] != "877"):
  print("CONTESTAR")

else:
  print("NO CONTESTAR")