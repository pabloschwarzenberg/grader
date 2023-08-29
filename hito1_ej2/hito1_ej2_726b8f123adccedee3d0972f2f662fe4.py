#Contestador de celular
print("Contestadora Automatica")
Num = int(input("Ingrese el numero Telefonico: "))
Ho = int(input("Ingrese Hora de la llamada: "))

if Num >= 1000000000:
  print("el numero escrito no es valido, intentelo de nuevo")
elif Ho < 0 or Ho > 23:
  print("La hora escrita no es valida, intentelo de nuevo")
elif Ho <= 7:
  print("Resultado: CONTESTAR")
elif Ho > 7 and Ho <= 14:
  Com = str(Num)
  B909 = Com.find("909")
  if B909 == 5:
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif Ho >= 17 and Ho <= 19:
  Com = str(Num)
  B877 = Com.find("877")
  if B877 == 0:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")
elif Ho > 19:
  print("Resultado: NO CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")   