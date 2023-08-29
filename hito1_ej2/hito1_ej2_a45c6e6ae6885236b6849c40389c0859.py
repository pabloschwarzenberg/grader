#Contestador de celular
print("Contestador Automatico")
Num = int(input("Ingrese el numero de Telefono: "))
Hora = int(input("Ingrese La hora de la llamada: "))

if Num >= 1000000000:
  print("el numero escrito es invalido, intentelo nuevamente")
elif Hora < 0 or Hora > 23:
  print("La hora escrita es invalida, intentelo nuevamente")
elif Hora <= 7:
  print("Resultado: CONTESTAR")
elif Hora > 7 and Hora <= 14:
  Com = str(Num)
  B909 = Com.find("909")
  if B909 == 5:
    print("Resultado: CONTESTAR")
  else:
    print("Resultado: NO CONTESTAR")
elif Hora >= 17 and Hora <= 19:
  Com = str(Num)
  B877 = Com.find("877")
  if B877 == 0:
    print("Resultado: NO CONTESTAR")
  else:
    print("Resultado: CONTESTAR")
elif Hora > 19:
  print("Resultado: NO CONTESTAR")
else:
  print("Resultado: NO CONTESTAR")  