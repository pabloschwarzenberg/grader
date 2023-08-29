num = int(input("Ingrese el numero Telefonico: "))
hor = int(input("Ingrese hora de la llamada: "))
if num >= 1000000000:
  print("no es valido, intentelo de nuevo")
elif hor < 0 or hor > 23:
  print("no es valida, intentelo de nuevo")
elif hor <= 7:
  print("Resultado: CONTESTAR")
elif hor > 7 and hor <= 14:
  com = str(num)
  B909 = com.find("909")
  if B909 == 5:
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif hor >= 17 and hor <= 19:
  com = str(num)
  B877 = com.find("877")
  if B877 == 0:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")
elif hor > 19:
  print("Resultado: NO CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")      