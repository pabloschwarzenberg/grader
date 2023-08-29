#Contestador de celular
hora = int(input("Por favor ingrese la hora (0 a 23): "))
telefono = int(input("Por favor ingrese el número de teléfono (8 dígitos): "))

# Verificar si es hora de la madrugada (00:00 a 07:00)
if hora >= 0 and hora < 7:
  print("CONTESTAR")

# Verificar si es antes de las 14:00 y el número termina en 909
elif hora >= 7 and hora < 14 and telefono % 1000 == 909:
  print("CONTESTAR")

# Verificar si es durante la tarde (17:00 a 19:00) y el número comienza por 877
elif hora >= 17 and hora < 19 and telefono // 1000000 == 877:
  print("CONTESTAR")

# Si no aplica ninguna de las condiciones anteriores, no contestar
else:
  print("NO CONTESTAR")     