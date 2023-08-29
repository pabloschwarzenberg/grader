#Contestador de celular
numte=int(input("Ingrese el numero telefonico: "))
hordd=int(input("Ingrese una hora del dia: "))
if len(str(numte)) > 8:
  print("Numero Invalido")
else:
  if hordd >=0 and hordd <=7:
    print("CONTESTAR")
  elif hordd   < 14 and str(numte)[5:] == "909":
    print("CONTESTAR")
  elif hordd  < 14 and str(numte)[5:] != "909":
      print("no contestar")   
  elif hordd  >=17 and hordd  <=19 and str(numte)[:3] != "877":
    print("CONTESTAR")
  elif hordd  >=17 and hordd  <=19 and str(numte)[:3] == "877":
    print("NO CONTESTAR")
  elif hordd  > 13 and hordd  < 17:
      print("no contestar")
  if hordd  > 19:
    print("NO CONTESTAR")
