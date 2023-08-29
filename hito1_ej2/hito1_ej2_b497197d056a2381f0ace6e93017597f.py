#Contestador de celular
tel = int(input("Ingrese su numero telefonico: "))
hora = int(input("Ingrese la hora de la llamada: "))
if hora > 0 and hora <= 7:
  resultado = "CONTESTAR"
elif hora > 7 and hora < 14:
  if tel % 1000 == 909:
    resultado = "CONTESTAR"
  else:
    resultado = "NO CONTESTAR"
elif hora >= 14 and hora < 17:
  resultado = "NO CONTESTAR"
elif hora >= 17 and hora <= 19:
  if tel - (tel % 1000000) == 877:
    resultado = "CONTESTAR"
  else:
    resultado = "NO CONTESTAR"
else:
  resultado = "NO CONTESTAR"

print(resultado)