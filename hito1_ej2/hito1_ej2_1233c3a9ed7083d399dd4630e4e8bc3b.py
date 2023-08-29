#Contestador de celular
celular = str(input("ingrese celular: "))
dia = int(input("ingrese la hora del dia: "))
ult_3 = celular[-3:]
pri_3 = celular[:3]
if 0 <= dia <= 7:
  print ("CONTESTAR")
elif 7 < dia <= 14:
  if ult_3 == "909":
    print("CONTESTAR")
  else:
    print ("NO CONTESTAR")
elif 17 <= dia <= 19:
  if pri_3 == "877":
    print ("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif 19 < dia:
  print ("NO CONTESTAR")
else:
  print("NO CONTESTAR")