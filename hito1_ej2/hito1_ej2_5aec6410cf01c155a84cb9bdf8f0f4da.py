#Contestador de celular
x = int(input("Ingrese numero telefonico"))
y = int(input("Ingrese hora de la llamada"))
x1 = x%1000
x2 = (int(x/100000))
if 0 <= y <= 7:
  print ("CONTESTAR")
elif (7 < y < 14) and (x1 == 909):
  print ("CONTESTAR")
elif (7 < y < 14) and (x1 != 909):
  print ("NO CONTESTAR")
elif (17<= y <= 19) and (x2 != 877):
  print ("CONTESTAR")
else:
  print ("NO CONTESTAR")